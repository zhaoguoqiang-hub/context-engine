"""Narrative tests."""
def test_append_and_last(acontext):
    acontext.narratives.append({"signal": "关键决策", "agent": "codex", "summary": "迁移到Remix", "ts": "2026-06-20T10:00:00Z", "tags": ["#决策"]})
    results = acontext.narratives.last(n=1)
    assert len(results) == 1
    assert results[0]["signal"] == "关键决策"

def test_search_by_tag(acontext):
    acontext.narratives.append({"signal": "关键决策", "agent": "codex", "summary": "X", "ts": "2026-01-01T00:00:00Z", "tags": ["#决策"]})
    acontext.narratives.append({"signal": "情绪转折", "agent": "codex", "summary": "Y", "ts": "2026-01-01T00:00:00Z", "tags": ["#情绪"]})
    results = acontext.narratives.search(tags=["#决策"])
    assert len(results) == 1
    assert results[0]["signal"] == "关键决策"

def test_empty_file(acontext):
    assert acontext.narratives.last() == []
    assert acontext.narratives.search() == []
