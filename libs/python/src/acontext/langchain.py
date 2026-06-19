"""LangChain memory adapter for AContext.

Usage:
    from acontext.langchain import AContextMemory
    memory = AContextMemory(context_path="~/.acontext", agent_id="codex")
"""
from __future__ import annotations
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from . import AContext


class AContextMemory:
    """Thin LangChain-compatible memory backed by AContext.

    Implements the informal LangChain memory interface:
    - load_memory_variables(inputs) -> dict
    - save_context(inputs, outputs) -> None

    Not a full BaseMemory subclass — AContext is agent context, not chat memory.
    This adapter bridges the gap for LangChain users.
    """

    def __init__(self, context_path: str = "~/.acontext", agent_id: str = "agent"):
        self._ctx = AContext(context_path)
        self._agent_id = agent_id

    def load_memory_variables(self, _inputs: dict[str, Any] | None = None) -> dict[str, str]:
        """Return current context as a single 'context' string."""
        parts: list[str] = []

        # Active goals
        goals_path = self._ctx.root / "goals.json"
        if goals_path.exists():
            goals_data = json.loads(goals_path.read_text())
            active = [g for g in goals_data.get("goals", []) if g.get("status") == "active"]
            if active:
                parts.append("## 活跃目标")
                for g in sorted(active, key=lambda x: x.get("priority", 0), reverse=True):
                    parts.append(f"- [{g['priority']}] {g['name']}")

        # Recent narratives
        recent = self._ctx.narratives.last(n=5)
        if recent:
            parts.append("## 最近事件")
            for e in recent:
                parts.append(f"- {e.get('ts','')[:10]} | {e.get('signal','')} | {e.get('summary','')}")

        # Profile snapshot
        profile = self._ctx.profile.read()
        if profile.get("preferences"):
            pref_str = ", ".join(p["value"] for p in profile["preferences"][:5])
            parts.append(f"## 用户偏好: {pref_str}")
        if profile.get("trivia"):
            trivia_str = ", ".join(t["detail"] for t in profile["trivia"][:3])
            parts.append(f"## 琐事: {trivia_str}")

        return {"context": "\n\n".join(parts) if parts else ""}

    def save_context(self, inputs: dict[str, Any], outputs: dict[str, Any]) -> None:
        """Save interaction to journals + narratives."""
        ts = datetime.now(timezone.utc).isoformat()
        user_msg = str(inputs.get("input", ""))
        ai_msg = str(outputs.get("output", ""))

        # Journal
        self._ctx.journals.append(self._agent_id, {
            "ts": ts, "mood": "task",
            "work": [f"User: {user_msg[:80]}", f"AI: {ai_msg[:80]}"],
        })

        # Narrative (if seems significant)
        if len(user_msg) > 50 or any(kw in user_msg for kw in ["决定", "完成", "部署", "发布", "迁移"]):
            self._ctx.narratives.append({
                "ts": ts,
                "signal": "关键决策",
                "agent": self._agent_id,
                "summary": user_msg[:120],
                "tags": [],
                "privacy": "public",
            })
