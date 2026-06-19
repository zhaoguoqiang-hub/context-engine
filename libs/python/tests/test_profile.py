"""Profile tests."""
import json

def test_empty_profile(acontext):
    p = acontext.profile.read()
    assert p["preferences"] == []
    assert p["_meta"]["v"] == "1.0"

def test_update_preferences(acontext):
    acontext.profile.update({"preferences": [{"value": "喜欢Obsidian", "source": "test", "added": "2026-06-20"}]})
    p = acontext.profile.read()
    assert len(p["preferences"]) == 1
    assert p["preferences"][0]["value"] == "喜欢Obsidian"

def test_set_field(acontext):
    acontext.profile.set_field("humorStyle", "谐音梗")
    assert acontext.profile.read()["humorStyle"] == "谐音梗"

def test_deep_merge(acontext):
    acontext.profile.update({"values": {"potential": [{"value": "隐私", "mentions": 1}]}})
    acontext.profile.update({"values": {"potential": [{"value": "效率", "mentions": 1}]}})
    p = acontext.profile.read()
    assert len(p["values"]["potential"]) == 2
