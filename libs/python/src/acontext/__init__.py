"""AContext — file-based, user-owned context layer for AI agents."""
from pathlib import Path
from .profile import ProfileManager
from .narratives import NarrativesManager
from .journals import JournalsManager
from .handoff import HandoffManager
from .meta import MetaManager


class AContext:
    """Main entry point for AContext operations.

    Usage:
        ctx = AContext("~/.acontext")
        ctx.profile.read()
        ctx.narratives.append({"signal": "关键决策", ...})
    """

    def __init__(self, path: str | Path = "~/.acontext"):
        self._root = Path(path).expanduser().resolve()
        self._root.mkdir(parents=True, exist_ok=True)
        self.profile = ProfileManager(self._root)
        self.narratives = NarrativesManager(self._root)
        self.journals = JournalsManager(self._root)
        self.handoff = HandoffManager(self._root)
        self.meta = MetaManager(self._root)

    @property
    def root(self) -> Path:
        return self._root
