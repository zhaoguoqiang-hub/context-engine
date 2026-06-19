"""Handoff manager — agent-to-agent envelopes."""
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


class HandoffManager:
    def __init__(self, path: Path):
        self._dir = path / "handoffs"
        self._dir.mkdir(parents=True, exist_ok=True)

    def _file(self, agent_id: str) -> Path:
        return self._dir / f"{agent_id}.json"

    def write(self, target: str, from_agent: str, *,
              completed: list[str] | None = None,
              pending: list[str] | None = None,
              needs: list[str] | None = None,
              files: list[str] | None = None,
              notes: str = "") -> None:
        envelope = {
            "from": from_agent, "to": target,
            "ts": datetime.now(timezone.utc).isoformat(),
            "completed": completed or [],
            "pending": pending or [],
            "needs": needs or [],
            "files": files or [],
            "notes": notes,
            "acknowledged": False
        }
        fp = self._file(target)
        existing: list[dict[str, Any]] = []
        if fp.exists():
            existing = json.loads(fp.read_text())
            if not isinstance(existing, list):
                existing = [existing]
        existing.append(envelope)
        tmp = fp.with_suffix(".tmp")
        tmp.write_text(json.dumps(existing, ensure_ascii=False, indent=2))
        tmp.rename(fp)

    def inbox(self, agent_id: str, unacknowledged_only: bool = True) -> list[dict[str, Any]]:
        fp = self._file(agent_id)
        if not fp.exists():
            return []
        envelopes = json.loads(fp.read_text())
        if not isinstance(envelopes, list):
            envelopes = [envelopes]
        if unacknowledged_only:
            return [e for e in envelopes if not e.get("acknowledged")]
        return envelopes

    def acknowledge(self, agent_id: str, index: int = 0) -> None:
        fp = self._file(agent_id)
        envelopes = json.loads(fp.read_text())
        if not isinstance(envelopes, list):
            envelopes = [envelopes]
        if 0 <= index < len(envelopes):
            envelopes[index]["acknowledged"] = True
            envelopes[index]["acknowledged_ts"] = datetime.now(timezone.utc).isoformat()
        tmp = fp.with_suffix(".tmp")
        tmp.write_text(json.dumps(envelopes, ensure_ascii=False, indent=2))
        tmp.rename(fp)
