"""
Entity reader — replaces ZepEntityReader with local NetworkX graph.
API-compatible with ZepEntityReader so callers need minimal changes.
"""

from typing import Any, Dict, List, Optional, Set
from dataclasses import dataclass, field

from ..utils.logger import get_logger
from . import nx_graph

logger = get_logger('mirofish.entity_reader')


@dataclass
class EntityNode:
    """Entity node data structure — same as old ZepEntityReader.EntityNode."""
    uuid: str
    name: str
    labels: List[str]
    summary: str
    attributes: Dict[str, Any]
    related_edges: List[Dict[str, Any]] = field(default_factory=list)
    related_nodes: List[Dict[str, Any]] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "uuid": self.uuid,
            "name": self.name,
            "labels": self.labels,
            "summary": self.summary,
            "attributes": self.attributes,
            "related_edges": self.related_edges,
            "related_nodes": self.related_nodes,
        }

    def get_entity_type(self) -> Optional[str]:
        for label in self.labels:
            if label not in ("Entity", "Node"):
                return label
        return None


@dataclass
class FilteredEntities:
    """Filtered entity collection."""
    entities: List[EntityNode]
    entity_types: Set[str]
    total_count: int
    filtered_count: int

    def to_dict(self) -> Dict[str, Any]:
        return {
            "entities": [e.to_dict() for e in self.entities],
            "entity_types": list(self.entity_types),
            "total_count": self.total_count,
            "filtered_count": self.filtered_count,
        }


class EntityReader:
    """
    Local entity reader backed by NetworkX/JSON graph store.
    Drop-in replacement for ZepEntityReader.
    """

    def get_all_nodes(self, graph_id: str) -> List[Dict[str, Any]]:
        """Return all nodes as plain dicts."""
        nodes = nx_graph.get_entities(graph_id)
        logger.info(f"get_all_nodes graph={graph_id}: {len(nodes)} nodes")
        return nodes

    def get_all_edges(self, graph_id: str) -> List[Dict[str, Any]]:
        """Return all edges as plain dicts."""
        edges = nx_graph.get_edges(graph_id)
        logger.info(f"get_all_edges graph={graph_id}: {len(edges)} edges")
        return edges

    def filter_defined_entities(
        self,
        graph_id: str,
        defined_entity_types: Optional[List[str]] = None,
        enrich_with_edges: bool = True,
    ) -> FilteredEntities:
        """
        Return entities that have a custom entity_type (non-generic).
        Optionally enriched with related edge/node info.
        """
        all_nodes = self.get_all_nodes(graph_id)
        total_count = len(all_nodes)

        all_edges = self.get_all_edges(graph_id) if enrich_with_edges else []

        # Build node map for quick lookup
        node_map = {n["uuid"]: n for n in all_nodes}

        filtered = []
        entity_types_found: Set[str] = set()

        for node in all_nodes:
            labels = node.get("labels", [])
            custom_labels = [l for l in labels if l not in ("Entity", "Node")]

            if not custom_labels:
                continue

            if defined_entity_types:
                matching = [l for l in custom_labels if l in defined_entity_types]
                if not matching:
                    continue
                entity_type = matching[0]
            else:
                entity_type = custom_labels[0]

            entity_types_found.add(entity_type)

            entity = EntityNode(
                uuid=node["uuid"],
                name=node.get("name", ""),
                labels=labels,
                summary=node.get("summary", ""),
                attributes=node.get("attributes", {}),
            )

            if enrich_with_edges:
                related_edges = []
                related_node_uuids: Set[str] = set()

                for edge in all_edges:
                    if edge.get("source_node_uuid") == node["uuid"]:
                        related_edges.append({
                            "direction": "outgoing",
                            "edge_name": edge.get("name", ""),
                            "fact": edge.get("fact", ""),
                            "target_node_uuid": edge.get("target_node_uuid", ""),
                        })
                        related_node_uuids.add(edge["target_node_uuid"])
                    elif edge.get("target_node_uuid") == node["uuid"]:
                        related_edges.append({
                            "direction": "incoming",
                            "edge_name": edge.get("name", ""),
                            "fact": edge.get("fact", ""),
                            "source_node_uuid": edge.get("source_node_uuid", ""),
                        })
                        related_node_uuids.add(edge["source_node_uuid"])

                entity.related_edges = related_edges
                entity.related_nodes = [
                    {
                        "uuid": node_map[uid]["uuid"],
                        "name": node_map[uid].get("name", ""),
                        "labels": node_map[uid].get("labels", []),
                        "summary": node_map[uid].get("summary", ""),
                    }
                    for uid in related_node_uuids
                    if uid in node_map
                ]

            filtered.append(entity)

        logger.info(
            f"filter_defined_entities graph={graph_id}: total={total_count}, "
            f"filtered={len(filtered)}, types={entity_types_found}"
        )
        return FilteredEntities(
            entities=filtered,
            entity_types=entity_types_found,
            total_count=total_count,
            filtered_count=len(filtered),
        )

    def get_entities_by_type(
        self,
        graph_id: str,
        entity_type: str,
        enrich_with_edges: bool = True,
    ) -> List[EntityNode]:
        """Return all entities of a specific type."""
        result = self.filter_defined_entities(
            graph_id=graph_id,
            defined_entity_types=[entity_type],
            enrich_with_edges=enrich_with_edges,
        )
        return result.entities

    def get_entity_with_context(
        self,
        graph_id: str,
        entity_uuid: str,
    ) -> Optional[EntityNode]:
        """Return a single entity with its related edges and nodes."""
        node = nx_graph.get_entity(graph_id, entity_uuid)
        if not node:
            return None

        all_edges = nx_graph.get_edges(graph_id)
        all_nodes = nx_graph.get_entities(graph_id)
        node_map = {n["uuid"]: n for n in all_nodes}

        related_edges = []
        related_node_uuids: Set[str] = set()

        for edge in all_edges:
            if edge.get("source_node_uuid") == entity_uuid:
                related_edges.append({
                    "direction": "outgoing",
                    "edge_name": edge.get("name", ""),
                    "fact": edge.get("fact", ""),
                    "target_node_uuid": edge.get("target_node_uuid", ""),
                })
                related_node_uuids.add(edge["target_node_uuid"])
            elif edge.get("target_node_uuid") == entity_uuid:
                related_edges.append({
                    "direction": "incoming",
                    "edge_name": edge.get("name", ""),
                    "fact": edge.get("fact", ""),
                    "source_node_uuid": edge.get("source_node_uuid", ""),
                })
                related_node_uuids.add(edge["source_node_uuid"])

        related_nodes = [
            {
                "uuid": node_map[uid]["uuid"],
                "name": node_map[uid].get("name", ""),
                "labels": node_map[uid].get("labels", []),
                "summary": node_map[uid].get("summary", ""),
            }
            for uid in related_node_uuids
            if uid in node_map
        ]

        return EntityNode(
            uuid=node["uuid"],
            name=node.get("name", ""),
            labels=node.get("labels", []),
            summary=node.get("summary", ""),
            attributes=node.get("attributes", {}),
            related_edges=related_edges,
            related_nodes=related_nodes,
        )


# Backwards compat alias
ZepEntityReader = EntityReader
