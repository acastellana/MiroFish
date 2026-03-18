"""
Graph builder service — replaces Zep Cloud with local NetworkX graph.

Graph build flow:
  text chunks → LLM extracts entities+relationships → stored in nx_graph (JSON)
"""

import json
import threading
import traceback
from typing import Any, Callable, Dict, List, Optional

from ..config import Config
from ..models.task import TaskManager, TaskStatus
from ..utils.logger import get_logger
from ..utils.llm_client import LLMClient
from .text_processor import TextProcessor
from . import nx_graph

logger = get_logger('mirofish.graph_builder')


class GraphInfo:
    """Graph metadata."""

    def __init__(self, graph_id: str, node_count: int, edge_count: int, entity_types: List[str]):
        self.graph_id = graph_id
        self.node_count = node_count
        self.edge_count = edge_count
        self.entity_types = entity_types

    def to_dict(self) -> Dict[str, Any]:
        return {
            "graph_id": self.graph_id,
            "node_count": self.node_count,
            "edge_count": self.edge_count,
            "entity_types": self.entity_types,
        }


# ---------------------------------------------------------------------------
# LLM extraction helpers
# ---------------------------------------------------------------------------

_EXTRACT_SYSTEM = """You are a knowledge graph extraction assistant.
Given a text chunk and an ontology, extract all entities and relationships.

Return a JSON object like:
{
  "entities": [
    {"name": "Alice", "type": "Person", "attributes": {"age": "30", "role": "teacher"}}
  ],
  "relationships": [
    {"source": "Alice", "source_type": "Person", "target": "School", "target_type": "Organization",
     "relation": "works_at", "fact": "Alice works at the local school."}
  ]
}

Rules:
- Only extract entities whose type is listed in the ontology entity_types.
- Only extract relationships whose type is listed in the ontology edge_types.
- entity names must be proper nouns or unique identifiers.
- If no entities or relationships found, return empty lists.
- Return only valid JSON, no markdown fences.
"""


def _extract_entities_and_relations(
    chunk: str,
    ontology: Dict[str, Any],
    llm: LLMClient,
) -> Dict[str, Any]:
    """Call LLM to extract entities+relations from a single text chunk."""
    entity_type_names = [e["name"] for e in ontology.get("entity_types", [])]
    edge_type_names = [e["name"] for e in ontology.get("edge_types", [])]

    user_msg = f"""Ontology:
Entity types: {entity_type_names}
Edge types: {edge_type_names}

Text chunk:
{chunk}

Extract entities and relationships following the ontology."""

    try:
        result = llm.chat_json(
            messages=[
                {"role": "system", "content": _EXTRACT_SYSTEM},
                {"role": "user", "content": user_msg},
            ],
            temperature=0.1,
        )
        return result
    except Exception as e:
        logger.warning(f"LLM extraction failed: {e}")
        return {"entities": [], "relationships": []}


# ---------------------------------------------------------------------------
# GraphBuilderService
# ---------------------------------------------------------------------------

class GraphBuilderService:
    """
    Builds a local NetworkX knowledge graph from text.
    API-compatible with the old Zep-based GraphBuilderService.
    """

    def __init__(self, api_key: Optional[str] = None):
        # api_key param kept for backward compat (ignored — no cloud needed)
        self._llm: Optional[LLMClient] = None
        self.task_manager = TaskManager()

    @property
    def llm(self) -> LLMClient:
        if self._llm is None:
            self._llm = LLMClient()
        return self._llm

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def create_graph(self, name: str) -> str:
        """Create a new graph (just mints an ID; nx_graph is lazy-init on first write)."""
        import uuid as _uuid
        graph_id = f"mirofish_{_uuid.uuid4().hex[:16]}"
        # Touch the graph so it's recognized as existing
        nx_graph.load(graph_id)
        logger.info(f"Created graph: {graph_id} (name={name})")
        return graph_id

    def set_ontology(self, graph_id: str, ontology: Dict[str, Any]):
        """Store ontology in graph metadata (persisted to disk as part of graph JSON)."""
        graph = nx_graph.load(graph_id)
        graph["ontology"] = ontology
        nx_graph.save(graph_id)
        logger.info(f"Ontology set for graph {graph_id}")

    def add_text_batches(
        self,
        graph_id: str,
        chunks: List[str],
        batch_size: int = 3,
        progress_callback: Optional[Callable] = None,
    ) -> List[str]:
        """
        Process text chunks, extract entities+relations, store in nx_graph.
        Returns list of processed chunk IDs (for API compat with old Zep version).
        """
        graph = nx_graph.load(graph_id)
        ontology = graph.get("ontology", {})
        total = len(chunks)
        chunk_ids = []

        for i, chunk in enumerate(chunks):
            progress = (i + 1) / total
            if progress_callback:
                progress_callback(f"Processing chunk {i+1}/{total}...", progress)

            extraction = _extract_entities_and_relations(chunk, ontology, self.llm)

            # Store entities
            name_to_uuid: Dict[str, str] = {}
            for ent in extraction.get("entities", []):
                name = str(ent.get("name", "")).strip()
                etype = str(ent.get("type", "")).strip()
                attrs = ent.get("attributes", {})
                if not name or not etype:
                    continue
                node_id = nx_graph.add_entity(graph_id, etype, name, attrs)
                name_to_uuid[f"{name}::{etype}"] = node_id
                name_to_uuid[name] = node_id  # fallback key

            # Store relationships
            for rel in extraction.get("relationships", []):
                src_name = str(rel.get("source", "")).strip()
                tgt_name = str(rel.get("target", "")).strip()
                src_type = str(rel.get("source_type", "")).strip()
                tgt_type = str(rel.get("target_type", "")).strip()
                relation = str(rel.get("relation", "")).strip()
                fact = str(rel.get("fact", "")).strip()

                src_id = name_to_uuid.get(f"{src_name}::{src_type}") or name_to_uuid.get(src_name)
                tgt_id = name_to_uuid.get(f"{tgt_name}::{tgt_type}") or name_to_uuid.get(tgt_name)

                if not src_id:
                    src_id = nx_graph.add_entity(graph_id, src_type or "Entity", src_name, {})
                    name_to_uuid[src_name] = src_id
                if not tgt_id:
                    tgt_id = nx_graph.add_entity(graph_id, tgt_type or "Entity", tgt_name, {})
                    name_to_uuid[tgt_name] = tgt_id

                if src_id and tgt_id and relation:
                    nx_graph.add_edge(graph_id, src_id, tgt_id, relation, {}, fact=fact)

            chunk_ids.append(str(i))

        # Save after processing all chunks
        nx_graph.save(graph_id)
        logger.info(f"Processed {total} chunks for graph {graph_id}")
        return chunk_ids

    def _wait_for_episodes(
        self,
        episode_uuids: List[str],
        progress_callback: Optional[Callable] = None,
        timeout: int = 600,
    ):
        """No-op: NetworkX processes synchronously, no waiting needed."""
        if progress_callback:
            progress_callback("Graph processing complete (local, no wait needed).", 1.0)

    def _get_graph_info(self, graph_id: str) -> GraphInfo:
        data = nx_graph.get_graph_data(graph_id)
        entity_types = set()
        for node in data["nodes"]:
            for label in node.get("labels", []):
                if label not in ("Entity", "Node"):
                    entity_types.add(label)
        return GraphInfo(
            graph_id=graph_id,
            node_count=data["node_count"],
            edge_count=data["edge_count"],
            entity_types=list(entity_types),
        )

    def get_graph_data(self, graph_id: str) -> Dict[str, Any]:
        """Return full graph data (nodes + edges)."""
        return nx_graph.get_graph_data(graph_id)

    def delete_graph(self, graph_id: str):
        """Delete a graph."""
        nx_graph.delete_graph(graph_id)
        logger.info(f"Deleted graph: {graph_id}")

    # ------------------------------------------------------------------
    # Async build (used by the API endpoint)
    # ------------------------------------------------------------------

    def build_graph_async(
        self,
        text: str,
        ontology: Dict[str, Any],
        graph_name: str = "MiroFish Graph",
        chunk_size: int = 500,
        chunk_overlap: int = 50,
        batch_size: int = 3,
    ) -> str:
        """Start async graph build. Returns task_id."""
        task_id = self.task_manager.create_task(
            task_type="graph_build",
            metadata={"graph_name": graph_name, "chunk_size": chunk_size, "text_length": len(text)},
        )
        thread = threading.Thread(
            target=self._build_graph_worker,
            args=(task_id, text, ontology, graph_name, chunk_size, chunk_overlap, batch_size),
            daemon=True,
        )
        thread.start()
        return task_id

    def _build_graph_worker(
        self,
        task_id: str,
        text: str,
        ontology: Dict[str, Any],
        graph_name: str,
        chunk_size: int,
        chunk_overlap: int,
        batch_size: int,
    ):
        try:
            self.task_manager.update_task(task_id, status=TaskStatus.PROCESSING, progress=5, message="Starting graph build...")

            graph_id = self.create_graph(graph_name)
            self.task_manager.update_task(task_id, progress=10, message=f"Graph created: {graph_id}")

            self.set_ontology(graph_id, ontology)
            self.task_manager.update_task(task_id, progress=15, message="Ontology set")

            chunks = TextProcessor.split_text(text, chunk_size, chunk_overlap)
            total_chunks = len(chunks)
            self.task_manager.update_task(task_id, progress=20, message=f"Split into {total_chunks} chunks")

            self.add_text_batches(
                graph_id,
                chunks,
                batch_size,
                lambda msg, prog: self.task_manager.update_task(
                    task_id, progress=20 + int(prog * 70), message=msg
                ),
            )

            graph_info = self._get_graph_info(graph_id)
            self.task_manager.complete_task(task_id, {
                "graph_id": graph_id,
                "graph_info": graph_info.to_dict(),
                "chunks_processed": total_chunks,
            })

        except Exception as e:
            error_msg = f"{str(e)}\n{traceback.format_exc()}"
            self.task_manager.fail_task(task_id, error_msg)
