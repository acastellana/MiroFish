"""
zep_entity_reader.py — compatibility shim.
All real logic has moved to entity_reader.py (NetworkX-backed).
"""
from .entity_reader import (
    EntityNode,
    FilteredEntities,
    EntityReader,
    EntityReader as ZepEntityReader,
)

__all__ = ["EntityNode", "FilteredEntities", "ZepEntityReader", "EntityReader"]
