"""Profile manager — JSON read/write/merge."""
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


class ProfileManager:
    def __init__(self, path: Path):
        self._path = path / "profile.json"

    def read(self) -> dict[str, Any]:
        if not self._path.exists():
            return self._empty()
        return json.loads(self._path.read_text())

    def update(self, updates: dict[str, Any]) -> None:
        current = self.read()
        merged = self._deep_merge(current, updates)
        merged.setdefault("_meta", {})
        merged["_meta"]["updated"] = datetime.now(timezone.utc).isoformat()
        merged["_meta"]["v"] = "1.0"
        self._atomic_write(merged)

    def set_field(self, key: str, value: Any) -> None:
        self.update({key: value})

    def _deep_merge(self, base: dict, updates: dict) -> dict:
        for k, v in updates.items():
            if k in base and isinstance(base[k], dict) and isinstance(v, dict):
                base[k] = self._deep_merge(base[k], v)
            elif k in base and isinstance(base[k], list) and isinstance(v, list):
                base[k].extend(v)
            else:
                base[k] = v
        return base

    def _atomic_write(self, data: dict) -> None:
        tmp = self._path.with_suffix(".tmp")
        tmp.write_text(json.dumps(data, ensure_ascii=False, indent=2))
        tmp.rename(self._path)

    @staticmethod
    def _empty() -> dict[str, Any]:
        return {
            "_meta": {"v": "1.0", "updated": ""},
            "preferences": [], "habits": [],
            "values": {"stable": [], "potential": []},
            "trivia": [], "humorStyle": "", "emotionalPatterns": [],
            "loveLanguage": "", "innerCritic": [], "avoidTopics": [],
            "skills": [], "goals": []
        }
