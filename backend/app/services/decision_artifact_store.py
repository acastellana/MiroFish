"""
DecisionArtifactStore — Point 4 (v2)

Persists and reads decision artifacts produced by forcing functions.
Each artifact is one line in decision_artifacts.jsonl (newline-delimited JSON).

execution_status values:
  EXECUTED              — forcing function ran AND JSON parsed cleanly
  EXECUTED_PARSE_FAILED — forcing function ran but JSON could not be parsed
  NOT_EXECUTED          — forcing function was registered but never ran

v2 additions:
  - Richer artifact schema: observed_event_text, candidate_targeted, substitute_used,
    pmf_classification, pmf_rule_applied
  - candidate_aggregation(): structured confirm/falsify/near-miss totals per candidate
  - retroactive_reclassify(): re-applies pmf_outcome_rules to all stored artifacts
    whenever rules change (e.g. after a rule correction)
  - Branch-level consistency checks on write()
"""

import json
import os
from datetime import datetime
from typing import Any, Dict, List, Optional

from ..config import Config
from ..utils.logger import get_logger

logger = get_logger('mirofish.decision_artifact_store')


# ──────────────────────────────────────────────────────────────────────────────
# Consistency gate
# ──────────────────────────────────────────────────────────────────────────────

def _check_consistency(artifact: Dict[str, Any]) -> Optional[str]:
    """
    Returns a warning string if the artifact violates a branch-level consistency rule,
    or None if it is consistent.

    Rules (item 5 from spec):
    - If consequence mentions 'payment remained blocked' → cannot be confirm
    - If consequence mentions 'cleared without GenLayer' or 'substitute won' → cannot be confirm
    - If workflow_cleared_without_genlayer=true (explicit field) → cannot be confirm
    - If payment_blocked=true (explicit field) → cannot be confirm
    """
    classification = artifact.get("pmf_classification") or artifact.get("classification", "")
    if classification != "confirm":
        return None  # Only confirms need checking

    consequence = (artifact.get("consequence") or "").lower()
    observed_event = (artifact.get("observed_event_text") or "").lower()

    block_phrases = [
        "payment remained blocked",
        "workflow remained blocked",
        "cleared without genlayer",
        "substitute won",
        "manual arbitration",
        "refund",
        "loss absorption",
    ]
    for phrase in block_phrases:
        if phrase in consequence or phrase in observed_event:
            return (
                f"CONSISTENCY VIOLATION: classification=confirm but consequence/event "
                f"contains '{phrase}'. Reclassifying as falsify."
            )

    if artifact.get("workflow_cleared_without_genlayer"):
        return "CONSISTENCY VIOLATION: workflow_cleared_without_genlayer=true but classification=confirm. Reclassifying as falsify."
    if artifact.get("payment_blocked_after_decision"):
        return "CONSISTENCY VIOLATION: payment_blocked_after_decision=true but classification=confirm. Reclassifying as falsify."

    return None


class DecisionArtifactStore:
    """
    Append-only store for decision artifacts.

    The file lives at <simulation_dir>/decision_artifacts.jsonl.
    If simulation_dir is not supplied, falls back to Config.UPLOAD_FOLDER.
    """

    FILENAME = "decision_artifacts.jsonl"

    def __init__(self, simulation_dir: Optional[str] = None):
        if simulation_dir:
            self.store_path = os.path.join(simulation_dir, self.FILENAME)
        else:
            self.store_path = os.path.join(Config.UPLOAD_FOLDER, self.FILENAME)
        os.makedirs(os.path.dirname(self.store_path), exist_ok=True)

    # ------------------------------------------------------------------ #
    # Write                                                                 #
    # ------------------------------------------------------------------ #

    def write(
        self,
        ff_id: str,
        round_num: int,
        owner_name: str,
        owner_agent_id: int,
        raw_response: str,
        parsed: Optional[Dict[str, Any]],
        parse_success: bool,
    ) -> Dict[str, Any]:
        """
        Append one artifact record to the JSONL file.

        Expects parsed to already contain (from the PMF re-classifier in
        run_twitter_simulation.py):
          - pmf_classification    (confirm / falsify / near-miss)
          - pmf_rule_applied      (True if rule-based; False if agent self-report)
          - observed_event_text   (human-readable [OBSERVED] sentence)
          - candidate_targeted    (e.g. 'A', 'B', ...)
          - substitute_used       (e.g. 'ClearRule', 'manual', 'VeritasProtocol', 'none')

        Runs branch-level consistency checks and corrects misclassifications.

        Returns the written record.
        """
        execution_status = "EXECUTED" if parse_success else "EXECUTED_PARSE_FAILED"

        artifact = parsed or {}

        # Branch-level consistency check
        if parse_success and artifact:
            violation = _check_consistency(artifact)
            if violation:
                logger.warning(f"[FF:{ff_id}] {violation}")
                artifact["pmf_classification"] = "falsify"
                artifact["consistency_correction"] = violation

        record = {
            "ff_id": ff_id,
            "round_num": round_num,
            "owner_name": owner_name,
            "owner_agent_id": owner_agent_id,
            "execution_status": execution_status,
            "parse_success": parse_success,
            "artifact": artifact,
            "raw_response": raw_response,
            "timestamp": datetime.utcnow().isoformat() + "Z",
        }

        with open(self.store_path, "a", encoding="utf-8") as f:
            f.write(json.dumps(record, ensure_ascii=False) + "\n")

        pmf_cls = artifact.get("pmf_classification", "unknown")
        candidate = artifact.get("candidate_targeted", "?")
        logger.info(
            f"DecisionArtifact written: ff_id={ff_id} round={round_num} "
            f"status={execution_status} owner={owner_name} "
            f"pmf={pmf_cls} candidate={candidate}"
        )
        return record

    # ------------------------------------------------------------------ #
    # Read                                                                  #
    # ------------------------------------------------------------------ #

    def read_all(self) -> List[Dict[str, Any]]:
        """Return every artifact record in the file (chronological order)."""
        if not os.path.exists(self.store_path):
            return []
        records = []
        with open(self.store_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    records.append(json.loads(line))
                except json.JSONDecodeError:
                    logger.warning(f"Skipping malformed line in {self.store_path}")
        return records

    def get_by_ff_id(self, ff_id: str) -> List[Dict[str, Any]]:
        """Return all artifact records for a specific forcing function id."""
        return [r for r in self.read_all() if r.get("ff_id") == ff_id]

    # ------------------------------------------------------------------ #
    # Summary helpers                                                       #
    # ------------------------------------------------------------------ #

    def execution_summary(self, known_ff_ids: List[str]) -> Dict[str, str]:
        """
        Returns a dict mapping ff_id -> execution_status.

        For ff_ids that have no record in the file the status is NOT_EXECUTED.
        """
        executed: Dict[str, str] = {}
        for record in self.read_all():
            fid = record.get("ff_id")
            if fid:
                executed[fid] = record.get("execution_status", "EXECUTED_PARSE_FAILED")

        result = {}
        for fid in known_ff_ids:
            result[fid] = executed.get(fid, "NOT_EXECUTED")
        return result

    def candidate_aggregation(self) -> Dict[str, Dict[str, Any]]:
        """
        Returns per-candidate structured totals across all stored artifacts.

        Shape:
        {
          "A": {
            "confirms": 2,
            "falsifies": 1,
            "near_misses": 0,
            "total_samples": 3,
            "ff_ids": ["FF1", "FF5"],
            "substitutes": {"manual": 1},
            "last_classification": "confirm",
            "examples": [
              {"ff_id": "FF1", "pmf_classification": "confirm",
               "observed_event_text": "...", "timestamp": "..."}
            ]
          },
          ...
        }
        """
        from collections import defaultdict
        buckets: Dict[str, Dict] = defaultdict(lambda: {
            "confirms": 0,
            "falsifies": 0,
            "near_misses": 0,
            "total_samples": 0,
            "ff_ids": [],
            "substitutes": {},
            "last_classification": None,
            "examples": [],
        })

        for record in self.read_all():
            art = record.get("artifact", {})
            candidate = art.get("candidate_targeted")
            if not candidate:
                continue

            pmf_cls = art.get("pmf_classification") or art.get("classification", "unknown")
            substitute = art.get("substitute_used") or "none"
            ff_id = record.get("ff_id", "?")

            b = buckets[candidate]
            b["total_samples"] += 1
            b["last_classification"] = pmf_cls

            if pmf_cls == "confirm":
                b["confirms"] += 1
            elif pmf_cls == "falsify":
                b["falsifies"] += 1
                # Track substitute
                b["substitutes"][substitute] = b["substitutes"].get(substitute, 0) + 1
            elif pmf_cls == "near-miss":
                b["near_misses"] += 1

            if ff_id not in b["ff_ids"]:
                b["ff_ids"].append(ff_id)

            b["examples"].append({
                "ff_id": ff_id,
                "round_num": record.get("round_num"),
                "pmf_classification": pmf_cls,
                "decision": art.get("decision"),
                "observed_event_text": art.get("observed_event_text", ""),
                "substitute_used": substitute,
                "timestamp": record.get("timestamp"),
            })

        # Derive per-candidate verdict
        for b in buckets.values():
            if b["confirms"] > 0:
                b["verdict"] = "CONFIRMED"
            elif b["near_misses"] > 0:
                b["verdict"] = "NEAR-MISS"
            elif b["falsifies"] > 0:
                b["verdict"] = "FALSIFIED"
            else:
                b["verdict"] = "UNTESTED"

        return dict(buckets)

    def retroactive_reclassify(
        self, ff_rules: Dict[str, Dict[str, Any]]
    ) -> Dict[str, int]:
        """
        Re-applies pmf_outcome_rules to all stored artifacts and rewrites the file.

        ff_rules: {ff_id: pmf_outcome_rules_dict}
          pmf_outcome_rules_dict keys: confirm_if, near_miss_if

        Returns a summary: {"reclassified": N, "unchanged": M, "total": N+M}
        """
        if not os.path.exists(self.store_path):
            return {"reclassified": 0, "unchanged": 0, "total": 0}

        records = self.read_all()
        reclassified = 0
        updated = []

        for record in records:
            art = record.get("artifact", {})
            ff_id = record.get("ff_id", "")
            rules = ff_rules.get(ff_id)

            if not rules or not art:
                updated.append(record)
                continue

            decision = art.get("decision", "")
            confirm_values = rules.get("confirm_if", [])
            near_miss_values = rules.get("near_miss_if", [])

            if decision in confirm_values:
                new_cls = "confirm"
            elif decision in near_miss_values:
                new_cls = "near-miss"
            else:
                new_cls = "falsify"

            old_cls = art.get("pmf_classification") or art.get("classification", "")
            if new_cls != old_cls:
                art["pmf_classification"] = new_cls
                art["classification"] = new_cls  # keep in sync for legacy readers
                art["pmf_rule_applied"] = True
                record["artifact"] = art
                reclassified += 1
                logger.info(
                    f"retroactive_reclassify: ff_id={ff_id} decision={decision} "
                    f"{old_cls!r} → {new_cls!r}"
                )

            # Also run consistency check after reclassification
            violation = _check_consistency(art)
            if violation:
                art["pmf_classification"] = "falsify"
                art["classification"] = "falsify"
                art["consistency_correction"] = violation
                record["artifact"] = art
                logger.warning(f"[FF:{ff_id}] retroactive consistency fix: {violation}")

            updated.append(record)

        # Rewrite file atomically
        tmp_path = self.store_path + ".tmp"
        with open(tmp_path, "w", encoding="utf-8") as f:
            for r in updated:
                f.write(json.dumps(r, ensure_ascii=False) + "\n")
        os.replace(tmp_path, self.store_path)

        total = len(records)
        return {"reclassified": reclassified, "unchanged": total - reclassified, "total": total}
