"""Handoff tests."""
def test_write_and_inbox(acontext):
    acontext.handoff.write("hermes", "codex", completed=["部署API"], pending=["集成测试"], notes="环境变量在.env")
    inbox = acontext.handoff.inbox("hermes")
    assert len(inbox) == 1
    assert inbox[0]["from"] == "codex"
    assert inbox[0]["completed"] == ["部署API"]
    assert not inbox[0]["acknowledged"]

def test_acknowledge(acontext):
    acontext.handoff.write("hermes", "codex", completed=["部署API"])
    acontext.handoff.acknowledge("hermes", 0)
    inbox = acontext.handoff.inbox("hermes")
    assert inbox == []  # all acknowledged
