"""AContext quickstart example."""
from pathlib import Path
from acontext import AContext

ctx = AContext("/tmp/demo_acontext")

# 1. Register agent
ctx.meta.register("codex", "开发+深度分析")
print("Agents:", ctx.meta.agents)

# 2. Update profile
ctx.profile.update({
    "preferences": [{"value": "喜欢直接风格", "source": "example", "added": "2026-06-20"}],
    "trivia": [{"detail": "夏天只喝冰美式", "source": "example"}]
})
ctx.profile.set_field("humorStyle", "谐音梗")
print("Profile humorStyle:", ctx.profile.read()["humorStyle"])

# 3. Append narrative
ctx.narratives.append({
    "ts": "2026-06-20T10:00:00Z", "signal": "关键决策",
    "agent": "codex", "summary": "用户决定使用AContext",
    "tags": ["#决策"]
})
print("Last narrative:", ctx.narratives.last(1)[0]["summary"])

# 4. Write journal
ctx.journals.append("codex", {"mood": "celebrate", "work": ["AContext v0.1 发布"]})
print("Last journal:", ctx.journals.last("codex")[0]["mood"])

# 5. Handoff to hermes
ctx.handoff.write("hermes", "codex",
    completed=["AContext Python库 v0.1"],
    pending=["LangChain插件测试", "publish to GitHub"],
    notes="代码在 outputs/acontext-py/")

inbox = ctx.handoff.inbox("hermes")
if inbox:
    print(f"Handoff pending: {len(inbox)} items")
    print(f"  From: {inbox[0]['from']}, Completed: {inbox[0]['completed']}")
    ctx.handoff.acknowledge("hermes", 0)

print("\nDone. Data stored at:", ctx.root)
