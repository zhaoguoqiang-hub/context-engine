"""Journal tests."""
def test_append_and_read(acontext):
    acontext.journals.append("codex", {"mood": "task", "work": ["部署API"]})
    results = acontext.journals.last("codex", n=1)
    assert len(results) == 1
    assert results[0]["mood"] == "task"
    assert results[0]["agent"] == "codex"

def test_sibling_read(acontext):
    acontext.journals.append("hermes", {"mood": "tender", "work": ["发布文章"]})
    results = acontext.journals.last_any("hermes", n=1)
    assert results[0]["agent"] == "hermes"
    assert results[0]["mood"] == "tender"
