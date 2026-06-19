"""AContext data types."""
from dataclasses import dataclass, field
from typing import Any

SPEC_VERSION = "1.0"


@dataclass
class ProfileEntry:
    context: str = "universal"
    expires: str | None = None
    value: str
    source: str
    added: str


@dataclass
class Goal:
    id: str
    name: str
    priority: int
    status: str = "active"
    progress: int = 0
    keywords: list[str] = field(default_factory=list)


@dataclass
class NarrativeEvent:
    ts: str
    signal: str
    agent: str
    summary: str
    context: str = ""
    impact: str = ""
    tags: list[str] = field(default_factory=list)
    privacy: str = "public"
    context: str = "universal"

    def to_dict(self) -> dict[str, Any]:
        return {k: v for k, v in self.__dict__.items() if v}


@dataclass
class JournalEntry:
    ts: str
    agent: str
    mood: str = "task"
    work: list[str] = field(default_factory=list)
    emotional_moments: list[str] = field(default_factory=list)
    patterns: list[str] = field(default_factory=list)
    profile_updates: list[str] = field(default_factory=list)
    todos: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {k: v for k, v in self.__dict__.items() if v or k in ("work", "emotional_moments", "patterns", "profile_updates", "todos")}


@dataclass
class HandoffEnvelope:
    from_agent: str
    to_agent: str
    ts: str
    completed: list[str] = field(default_factory=list)
    pending: list[str] = field(default_factory=list)
    needs: list[str] = field(default_factory=list)
    files: list[str] = field(default_factory=list)
    notes: str = ""
    acknowledged: bool = False
    acknowledged_ts: str = ""

    def to_dict(self) -> dict[str, Any]:
        d = {
            "from": self.from_agent, "to": self.to_agent, "ts": self.ts,
            "completed": self.completed, "pending": self.pending,
            "needs": self.needs, "files": self.files, "notes": self.notes,
            "acknowledged": self.acknowledged
        }
        if self.acknowledged_ts:
            d["acknowledged_ts"] = self.acknowledged_ts
        return d


@dataclass
class FeedbackEntry:
    ts: str
    agent: str
    mode: str
    trigger: str
    result: str  # "+" | "-" | "="
    context: str = "universal"
    recency_weight: float = 1.0
    switch_to: str | None = None

    def to_dict(self) -> dict[str, Any]:
        return {k: v for k, v in self.__dict__.items() if v is not None}
