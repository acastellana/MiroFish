"""
NetworkX Graph Store — replaces Zep Cloud for local graph persistence.

Each graph is a NetworkX DiGraph serialized to JSON at:
  uploads/graphs/<graph_id>.json

Supported operations:
  add_entity(graph_id, entity_type, entity_name, attributes) → node_id (str uuid)
  add_edge(graph_id, source_id, target_id, edge_type, attributes)
  get_entities(graph_id, entity_type=None) → list[dict]
  get_edges(graph_id) → list[dict]
  get_entity(graph_id, node_id) → dict | None
  get_graph_data(graph_id) → {nodes, edges, node_count, edge_count}
  save(graph_id) / load(graph_id)
"""

import json
import os
import threading
import uuid
from typing import Any, Dict, List, Optional

from ..utils.logger import get_logger

logger = get_logger('mirofish.nx_graph')

# Base directory for graph files (relative to this file: ../uploads/graphs/)
_GRAPHS_DIR = os.path.join(os.path.dirname(__file__), '..', 'uploads', 'graphs')


def _graph_path(graph_id: str) -> str:
    return os.path.join(_GRAPHS_DIR, f"{graph_id}.json")


# In-memory cache: graph_id → {"nodes": {node_id: {...}}, "edges": [...]}
_cache: Dict[str, Dict[str, Any]] = {}
_lock = threading.Lock()


def _ensure_graphs_dir():
    os.makedirs(_GRAPHS_DIR, exist_ok=True)


def load(graph_id: str) -> Dict[str, Any]:
    """Load graph from disk (or return empty graph if not found)."""
    with _lock:
        if graph_id in _cache:
            return _cache[graph_id]

        path = _graph_path(graph_id)
        if os.path.exists(path):
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                _cache[graph_id] = data
                logger.info(f"Loaded graph {graph_id}: {len(data.get('nodes', {}))} nodes, {len(data.get('edges', []))} edges")
                return data
            except Exception as e:
                logger.warning(f"Failed to load graph {graph_id}: {e}")

        # Return empty graph structure
        empty = {"nodes": {}, "edges": []}
        _cache[graph_id] = empty
        return empty


def save(graph_id: str):
    """Persist current in-memory graph to disk."""
    _ensure_graphs_dir()
    with _lock:
        data = _cache.get(graph_id, {"nodes": {}, "edges": []})
        path = _graph_path(graph_id)
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        logger.debug(f"Saved graph {graph_id} to {path}")


def add_entity(
    graph_id: str,
    entity_type: str,
    entity_name: str,
    attributes: Optional[Dict[str, Any]] = None,
) -> str:
    """
    Add (or update) an entity node. Returns the node_id (uuid string).
    If an entity with the same name+type exists, returns existing node_id.
    """
    graph = load(graph_id)
    nodes = graph["nodes"]

    # Dedup by name+type
    for node_id, node in nodes.items():
        if node.get("name") == entity_name and node.get("entity_type") == entity_type:
            # Update attributes if new ones provided
            if attributes:
                node["attributes"].update(attributes)
            return node_id

    node_id = str(uuid.uuid4())
    nodes[node_id] = {
        "uuid": node_id,
        "name": entity_name,
        "entity_type": entity_type,
        "labels": ["Entity", entity_type],
        "summary": "",
        "attributes": attributes or {},
    }
    logger.debug(f"add_entity graph={graph_id} type={entity_type} name={entity_name} → {node_id}")
    return node_id


def add_edge(
    graph_id: str,
    source_id: str,
    target_id: str,
    edge_type: str,
    attributes: Optional[Dict[str, Any]] = None,
    fact: str = "",
):
    """Add a directed edge between two nodes."""
    graph = load(graph_id)
    edge_id = str(uuid.uuid4())
    graph["edges"].append({
        "uuid": edge_id,
        "name": edge_type,
        "fact": fact,
        "source_node_uuid": source_id,
        "target_node_uuid": target_id,
        "attributes": attributes or {},
    })
    logger.debug(f"add_edge graph={graph_id} {source_id[:8]}→{target_id[:8]} type={edge_type}")


def get_entities(
    graph_id: str,
    entity_type: Optional[str] = None,
) -> List[Dict[str, Any]]:
    """Return all entity nodes, optionally filtered by entity_type."""
    graph = load(graph_id)
    nodes = list(graph["nodes"].values())
    if entity_type:
        nodes = [n for n in nodes if n.get("entity_type") == entity_type]
    return nodes


def get_edges(graph_id: str) -> List[Dict[str, Any]]:
    """Return all edges for a graph."""
    graph = load(graph_id)
    return list(graph["edges"])


def get_entity(graph_id: str, node_id: str) -> Optional[Dict[str, Any]]:
    """Return a single node by UUID, or None if not found."""
    graph = load(graph_id)
    return graph["nodes"].get(node_id)


def get_graph_data(graph_id: str) -> Dict[str, Any]:
    """
    Return full graph data compatible with the old Zep get_graph_data shape.
    """
    graph = load(graph_id)
    nodes_raw = list(graph["nodes"].values())
    edges_raw = list(graph["edges"])

    # Build node name lookup
    node_map = {n["uuid"]: n.get("name", "") for n in nodes_raw}

    nodes_data = []
    for n in nodes_raw:
        nodes_data.append({
            "uuid": n["uuid"],
            "name": n.get("name", ""),
            "labels": n.get("labels", ["Entity"]),
            "summary": n.get("summary", ""),
            "attributes": n.get("attributes", {}),
            "created_at": None,
        })

    edges_data = []
    for e in edges_raw:
        edges_data.append({
            "uuid": e["uuid"],
            "name": e.get("name", ""),
            "fact": e.get("fact", ""),
            "fact_type": e.get("name", ""),
            "source_node_uuid": e.get("source_node_uuid", ""),
            "target_node_uuid": e.get("target_node_uuid", ""),
            "source_node_name": node_map.get(e.get("source_node_uuid", ""), ""),
            "target_node_name": node_map.get(e.get("target_node_uuid", ""), ""),
            "attributes": e.get("attributes", {}),
            "created_at": None,
            "valid_at": None,
            "invalid_at": None,
            "expired_at": None,
            "episodes": [],
        })

    return {
        "graph_id": graph_id,
        "nodes": nodes_data,
        "edges": edges_data,
        "node_count": len(nodes_data),
        "edge_count": len(edges_data),
    }


def graph_exists(graph_id: str) -> bool:
    """Check if a graph file exists on disk."""
    return os.path.exists(_graph_path(graph_id))


def delete_graph(graph_id: str):
    """Remove graph from cache and disk."""
    with _lock:
        _cache.pop(graph_id, None)
    path = _graph_path(graph_id)
    if os.path.exists(path):
        os.remove(path)
        logger.info(f"Deleted graph file: {path}")
