"""Meta manager — agent registry."""
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


class MetaManager:
    def __init__(self, path: Path):
        self._path = path / "META.json"

    def read(self) -> dict[str, Any]:
        if not self._path.exists():
            return self._empty()
        return json.loads(self._path.read_text())

    @property
    def agents(self) -> dict[str, Any]:
        return self.read().get("agents", {})

    def register(self, agent_id: str, role: str) -> None:
        data = self.read()
        data["agents"][agent_id] = {"id": agent_id, "role": role, "active": True}
        data["_meta"]["updated"] = datetime.now(timezone.utc).isoformat()
        tmp = self._path.with_suffix(".tmp")
        tmp.write_text(json.dumps(data, ensure_ascii=False, indent=2))
        tmp.rename(self._path)

    @staticmethod
    def _empty() -> dict[str, Any]:
        return {"_meta": {"v": "1.0", "updated": ""}, "agents": {}}
