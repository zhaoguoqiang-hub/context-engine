"""Journals manager — per-agent JSONL."""
import json
from pathlib import Path
from typing import Any


class JournalsManager:
    def __init__(self, path: Path):
        self._dir = path / "journals"
        self._dir.mkdir(parents=True, exist_ok=True)

    def _file(self, agent_id: str) -> Path:
        return self._dir / f"{agent_id}.jsonl"

    def append(self, agent_id: str, entry: dict[str, Any]) -> None:
        entry.setdefault("agent", agent_id)
        line = json.dumps(entry, ensure_ascii=False) + "\n"
        fp = self._file(agent_id)
        tmp = fp.with_suffix(".tmp")
        if fp.exists():
            tmp.write_text(fp.read_text() + line)
        else:
            tmp.write_text(line)
        tmp.rename(fp)

    def last(self, agent_id: str, n: int = 1) -> list[dict[str, Any]]:
        fp = self._file(agent_id)
        if not fp.exists():
            return []
        lines = fp.read_text().strip().split("\n")
        results = []
        for ln in lines[-n:]:
            if ln.strip():
                try:
                    results.append(json.loads(ln))
                except json.JSONDecodeError:
                    pass
        return results

    def last_any(self, agent_id: str, n: int = 1) -> list[dict[str, Any]]:
        """Read sibling agent's journal (cross-agent awareness)."""
        return self.last(agent_id, n)
