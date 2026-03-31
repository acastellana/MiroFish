#!/usr/bin/env python3
"""
test_ff1.py — FF1 vertical slice test

1. Validates test config structure
2. Sets up a minimal sim environment pointing to test_ff1_vertical_slice.json
3. Verifies decision_artifacts.jsonl is created (or would be) with correct schema
4. If an existing decision_artifacts.jsonl is present (from a prior run), reads and validates it
5. Prints a full pass/fail report

Usage:
    cd /home/albert/clawd/projects/mirofish/backend
    python3 scripts/test_ff1.py

    # To run the actual simulation (requires OASIS env + LLM key):
    python3 scripts/test_ff1.py --run-sim
"""

import argparse
import json
import os
import sys

_scripts_dir = os.path.dirname(os.path.abspath(__file__))
_backend_dir = os.path.abspath(os.path.join(_scripts_dir, ".."))
_project_root = os.path.abspath(os.path.join(_backend_dir, ".."))
sys.path.insert(0, _backend_dir)

# Load .env
try:
    from dotenv import load_dotenv
    _env_file = os.path.join(_project_root, ".env")
    if os.path.exists(_env_file):
        load_dotenv(_env_file)
    else:
        _backend_env = os.path.join(_backend_dir, ".env")
        if os.path.exists(_backend_env):
            load_dotenv(_backend_env)
except ImportError:
    pass

CONFIG_PATH = os.path.join(_backend_dir, "test_ff1_vertical_slice.json")
REQUIRED_ARTIFACT_SCHEMA = ["decision", "reason", "substitute_rejected", "consequence", "classification"]
PASS = "✅"
FAIL = "❌"
WARN = "⚠️ "


def load_config() -> dict:
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def check_config(cfg: dict) -> list:
    """Structural validation of the test config. Returns list of (pass, msg) tuples."""
    results = []

    # Basic fields
    for field in ["simulation_id", "project_id", "agent_configs", "event_config", "time_config"]:
        ok = field in cfg
        results.append((ok, f"Config has '{field}'"))

    # Agent count (15 named agents + up to N org agents)
    agents = cfg.get("agent_configs", [])
    results.append((len(agents) >= 5, f"At least 5 agents configured (found {len(agents)})"))

    # FF decision owners present (named by role, not generic "decision_owner")
    ff_owners = [a for a in agents if a.get("decision_role", "") and "ff" in a.get("decision_role", "").lower()]
    results.append((len(ff_owners) >= 1, f"At least 1 FF-role agent (found {len(ff_owners)})"))

    marcus = next((a for a in agents if a.get("entity_name") == "Marcus Chen"), None)
    results.append((marcus is not None, "Marcus Chen agent exists"))

    # FF1 in event_config
    ffs = cfg.get("event_config", {}).get("forcing_functions", [])
    ff1 = next((f for f in ffs if f.get("id") == "FF1"), None)
    results.append((ff1 is not None, "FF1 forcing function defined in event_config"))

    if ff1:
        results.append((ff1.get("trigger_round") == 3, f"FF1 triggers at round 3 (got {ff1.get('trigger_round')})"))
        results.append((ff1.get("owner_entity_name") == "Marcus Chen", f"FF1 owner is Marcus Chen"))
        schema = ff1.get("required_schema", [])
        schema_ok = all(k in schema for k in REQUIRED_ARTIFACT_SCHEMA)
        results.append((schema_ok, f"FF1 required_schema has all 5 keys: {schema}"))

    # Time config: at least 10 rounds (support various sim lengths)
    tc = cfg.get("time_config", {})
    total_rounds = (tc.get("total_simulation_hours", 0) * 60) // tc.get("minutes_per_round", 60)
    results.append((total_rounds >= 10, f"Simulation has ≥10 rounds (got {total_rounds})"))

    # Twitter-only (no reddit)
    results.append((cfg.get("reddit_config") is None, "reddit_config is null (Twitter-only)"))
    results.append((cfg.get("twitter_config") is not None, "twitter_config present"))

    return results


def find_artifact_store(cfg: dict):
    """Return the path to decision_artifacts.jsonl for this simulation."""
    from app.config import Config
    simulation_id = cfg.get("simulation_id", "test_ff1_slice")
    sim_dir = os.path.join(Config.OASIS_SIMULATION_DATA_DIR, simulation_id)
    return os.path.join(sim_dir, "decision_artifacts.jsonl"), sim_dir


def check_artifacts(artifact_path: str, cfg: dict) -> list:
    """Validate artifacts in decision_artifacts.jsonl. Returns (pass, msg) tuples."""
    results = []

    if not os.path.exists(artifact_path):
        results.append((False, f"decision_artifacts.jsonl not found at {artifact_path} (run simulation first)"))
        return results

    records = []
    with open(artifact_path, "r", encoding="utf-8") as f:
        for i, line in enumerate(f):
            line = line.strip()
            if not line:
                continue
            try:
                records.append(json.loads(line))
            except json.JSONDecodeError as e:
                results.append((False, f"Line {i+1} is invalid JSON: {e}"))

    results.append((len(records) > 0, f"decision_artifacts.jsonl has {len(records)} record(s)"))

    ff1_records = [r for r in records if r.get("ff_id") == "FF1"]
    results.append((len(ff1_records) >= 1, f"At least 1 FF1 artifact found (got {len(ff1_records)})"))

    for rec in ff1_records:
        round_num = rec.get("round_num")
        results.append((round_num == 3, f"FF1 artifact triggered at round 3 (got round_num={round_num})"))

        results.append((rec.get("owner_name") == "Marcus Chen", f"FF1 artifact owner is Marcus Chen"))

        status = rec.get("execution_status")
        results.append((status in ("EXECUTED", "EXECUTED_PARSE_FAILED"),
                         f"FF1 execution_status is EXECUTED or EXECUTED_PARSE_FAILED (got {status})"))

        artifact = rec.get("artifact", {})
        if rec.get("parse_success"):
            for key in REQUIRED_ARTIFACT_SCHEMA:
                results.append((key in artifact, f"FF1 artifact has field '{key}' = {artifact.get(key, '<MISSING>')}"))

            decision_val = artifact.get("decision", "")
            valid_decisions = ["accept_genlayer", "reject_genlayer", "escalate_manual"]
            results.append((decision_val in valid_decisions,
                             f"FF1 decision value valid: '{decision_val}' in {valid_decisions}"))

            classification = artifact.get("classification", "")
            valid_cls = ["confirm", "falsify", "near-miss"]
            results.append((classification in valid_cls,
                             f"FF1 classification valid: '{classification}' in {valid_cls}"))
        else:
            results.append((False, f"FF1 parse_success=False — raw_response: {str(rec.get('raw_response', ''))[:200]}"))

    return results


def verify_store_import():
    """Verify DecisionArtifactStore can be imported cleanly."""
    try:
        from app.services.decision_artifact_store import DecisionArtifactStore
        return [(True, "DecisionArtifactStore imports OK")]
    except ImportError as e:
        return [(False, f"DecisionArtifactStore import failed: {e}")]


def verify_config_generator():
    """Verify forcing_functions survive round-trip through EventConfig."""
    try:
        from app.services.simulation_config_generator import EventConfig
        ec = EventConfig(
            forcing_functions=[{"id": "FF1", "trigger_round": 3, "owner_entity_name": "Marcus Chen"}]
        )
        ok = len(ec.forcing_functions) == 1 and ec.forcing_functions[0]["id"] == "FF1"
        return [(ok, "EventConfig.forcing_functions round-trip OK")]
    except Exception as e:
        return [(False, f"EventConfig test failed: {e}")]


def run_simulation_subprocess(config_path: str):
    """Run the simulation using run_twitter_simulation.py --no-wait."""
    import subprocess
    print("\n" + "="*60)
    print("Running simulation (--no-wait, max 12 rounds)...")
    print("="*60)
    cmd = [
        sys.executable,
        os.path.join(_scripts_dir, "run_twitter_simulation.py"),
        "--config", config_path,
        "--no-wait",
        "--max-rounds", "12",
    ]
    result = subprocess.run(cmd, capture_output=False)
    return result.returncode == 0


def print_results(title: str, results: list):
    print(f"\n── {title} ──")
    pass_count = sum(1 for ok, _ in results if ok)
    for ok, msg in results:
        icon = PASS if ok else FAIL
        print(f"  {icon}  {msg}")
    print(f"  → {pass_count}/{len(results)} passed")
    return pass_count, len(results)


def main():
    parser = argparse.ArgumentParser(description="FF1 vertical slice test")
    parser.add_argument("--run-sim", action="store_true",
                        help="Actually run the simulation (requires OASIS env + LLM_API_KEY)")
    parser.add_argument("--config", default=CONFIG_PATH,
                        help="Path to simulation config JSON")
    args = parser.parse_args()

    config_path = args.config
    print(f"\n{'='*60}")
    print(f"FF1 Vertical Slice Test")
    print(f"Config: {config_path}")
    print(f"{'='*60}")

    # 1. Load and check config
    try:
        cfg = load_config() if config_path == CONFIG_PATH else json.load(open(config_path))
    except Exception as e:
        print(f"{FAIL} Cannot load config: {e}")
        sys.exit(1)

    total_pass = 0
    total_tests = 0

    p, t = print_results("Config structure", check_config(cfg))
    total_pass += p; total_tests += t

    p, t = print_results("Module imports", verify_store_import())
    total_pass += p; total_tests += t

    p, t = print_results("EventConfig round-trip", verify_config_generator())
    total_pass += p; total_tests += t

    # 2. Optionally run the simulation
    if args.run_sim:
        sim_ok = run_simulation_subprocess(config_path)
        print_results("Simulation run", [(sim_ok, "Simulation exited cleanly (returncode=0)")])

    # 3. Check artifacts (from previous or just-run simulation)
    try:
        artifact_path, sim_dir = find_artifact_store(cfg)
        print(f"\n  Looking for artifacts at: {artifact_path}")
        p, t = print_results("Artifact schema validation", check_artifacts(artifact_path, cfg))
        total_pass += p; total_tests += t

        # Print raw artifact contents
        if os.path.exists(artifact_path):
            print(f"\n── decision_artifacts.jsonl contents ──")
            with open(artifact_path, "r", encoding="utf-8") as f:
                for i, line in enumerate(f):
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        rec = json.loads(line)
                        print(f"\n  [Record {i+1}]")
                        print(f"    ff_id:            {rec.get('ff_id')}")
                        print(f"    round_num:        {rec.get('round_num')}")
                        print(f"    owner_name:       {rec.get('owner_name')}")
                        print(f"    execution_status: {rec.get('execution_status')}")
                        print(f"    parse_success:    {rec.get('parse_success')}")
                        artifact = rec.get("artifact", {})
                        for key in REQUIRED_ARTIFACT_SCHEMA:
                            print(f"    {key}: {artifact.get(key, '<MISSING>')}")
                    except Exception:
                        print(f"  [Record {i+1}] (parse error)")
    except Exception as e:
        print(f"\n{WARN} Could not check artifacts: {e}")

    # 4. Summary
    print(f"\n{'='*60}")
    all_pass = total_pass == total_tests
    icon = PASS if all_pass else FAIL
    print(f"{icon} Final: {total_pass}/{total_tests} checks passed")
    print(f"{'='*60}\n")

    sys.exit(0 if all_pass else 1)


if __name__ == "__main__":
    main()
