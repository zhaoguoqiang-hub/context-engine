"""Narratives manager — JSONL append/search."""
import json
from pathlib import Path
from typing import Any


class NarrativesManager:
    def __init__(self, path: Path):
        self._path = path / "narratives.jsonl"

    def append(self, entry: dict[str, Any]) -> None:
        line = json.dumps(entry, ensure_ascii=False) + "\n"
        tmp = self._path.with_suffix(".tmp")
        if self._path.exists():
            tmp.write_text(self._path.read_text() + line)
        else:
            tmp.write_text(line)
        tmp.rename(self._path)

    def last(self, n: int = 3) -> list[dict[str, Any]]:
        if not self._path.exists():
            return []
        lines = self._path.read_text().strip().split("\n")
        return [self._safe_parse(l) for l in lines[-n:] if l.strip()]

    def search(self, tags: list[str] | None = None, agent: str | None = None,
               limit: int = 10) -> list[dict[str, Any]]:
        if not self._path.exists():
            return []
        results = []
        with open(self._path) as f:
            for line in f:
                if not line.strip():
                    continue
                entry = self._safe_parse(line)
                if not entry:
                    continue
                if tags and not any(t in entry.get("tags", []) for t in tags):
                    continue
                if agent and entry.get("agent") != agent:
                    continue
                results.append(entry)
                if len(results) >= limit:
                    break
        return results

    @staticmethod
    def _safe_parse(line: str) -> dict[str, Any] | None:
        try:
            return json.loads(line)
        except json.JSONDecodeError:
            return None
