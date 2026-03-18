"""
Zep Graph Memory Updater — stubbed out.

enable_graph_memory_update=False in all simulation runs, so this is a no-op.
Keeping the module so imports from simulation runner don't break.
"""

import threading
from typing import Any, Dict, List, Optional
from dataclasses import dataclass
from datetime import datetime

from ..utils.logger import get_logger

logger = get_logger('mirofish.zep_graph_memory_updater')


@dataclass
class AgentActivity:
    """Agent activity record (stub)."""
    platform: str
    agent_id: int
    agent_name: str
    action_type: str
    action_args: Dict[str, Any]
    round_num: int
    timestamp: str

    def to_episode_text(self) -> str:
        return f"{self.agent_name}: {self.action_type}"


class ZepGraphMemoryUpdater:
    """No-op stub. Graph memory updates are disabled."""

    def __init__(self, graph_id: str, api_key: Optional[str] = None):
        self.graph_id = graph_id
        self._running = False
        logger.info(f"ZepGraphMemoryUpdater (stub/no-op) init: graph_id={graph_id}")

    def start(self):
        self._running = True

    def stop(self):
        self._running = False

    def add_activity(self, activity: AgentActivity):
        pass  # no-op

    def add_activity_from_dict(self, data: Dict[str, Any], platform: str):
        pass  # no-op

    def get_stats(self) -> Dict[str, Any]:
        return {
            "graph_id": self.graph_id,
            "stub": True,
            "running": self._running,
        }


class ZepGraphMemoryManager:
    """No-op stub manager."""

    _updaters: Dict[str, ZepGraphMemoryUpdater] = {}
    _lock = threading.Lock()
    _stop_all_done = False

    @classmethod
    def create_updater(cls, simulation_id: str, graph_id: str) -> ZepGraphMemoryUpdater:
        with cls._lock:
            updater = ZepGraphMemoryUpdater(graph_id)
            updater.start()
            cls._updaters[simulation_id] = updater
        return updater

    @classmethod
    def get_updater(cls, simulation_id: str) -> Optional[ZepGraphMemoryUpdater]:
        return cls._updaters.get(simulation_id)

    @classmethod
    def stop_updater(cls, simulation_id: str):
        with cls._lock:
            updater = cls._updaters.pop(simulation_id, None)
            if updater:
                updater.stop()

    @classmethod
    def stop_all(cls):
        if cls._stop_all_done:
            return
        cls._stop_all_done = True
        with cls._lock:
            cls._updaters.clear()

    @classmethod
    def get_all_stats(cls) -> Dict[str, Dict[str, Any]]:
        return {sid: u.get_stats() for sid, u in cls._updaters.items()}
