# AContext

File-based, user-owned, cross-platform context layer for AI agents.

```bash
pip install acontext
```

## 3-Minute Quickstart

```python
from acontext import AContext

ctx = AContext("~/.acontext")

# 用户画像
ctx.profile.update({"preferences": [{"value": "喜欢Obsidian", "source": "manual", "added": "2026-06-20"}]})
ctx.profile.set_field("humorStyle", "谐音梗")

# 叙事记忆（append-only）
ctx.narratives.append({
    "ts": "2026-06-20T10:00:00Z", "signal": "关键决策",
    "agent": "codex", "summary": "决定迁移到Remix",
    "tags": ["#决策", "#技术选型"]
})

# 最后3条
for e in ctx.narratives.last(3):
    print(e["summary"])

# 按标签搜索
for e in ctx.narratives.search(tags=["#决策"]):
    print(e["summary"])

# Agent 日志
ctx.journals.append("codex", {"mood": "task", "work": ["部署API服务"]})
ctx.journals.last("codex", n=1)

# Agent 交接
ctx.handoff.write("hermes", "codex",
    completed=["部署user-service到staging"],
    pending=["集成测试"],
    notes="环境变量在.env.staging")
inbox = ctx.handoff.inbox("hermes")
ctx.handoff.acknowledge("hermes", 0)
```

## LangChain Adapter

```python
from acontext.langchain import AContextMemory

memory = AContextMemory(context_path="~/.acontext", agent_id="codex")
context = memory.load_memory_variables({})  # -> {"context": "..."}
memory.save_context({"input": "帮我部署"}, {"output": "已部署"})
```

## Design

- **Zero dependencies** — stdlib only
- **JSON + JSONL** — any language can read/write
- **Atomic writes** — tmp file then rename
- **Lazy loading** — `last()` reads from file tail, `append()` writes one line
- **No server** — flat files in `~/.acontext/`

## API

| Manager | Methods |
|---------|---------|
| `ctx.profile` | `read()`, `update(dict)`, `set_field(key, value)` |
| `ctx.narratives` | `append(dict)`, `last(n=3)`, `search(tags, agent, limit)` |
| `ctx.journals` | `append(agent_id, dict)`, `last(agent_id, n)`, `last_any(agent_id, n)` |
| `ctx.handoff` | `write(target, from, ...)`, `inbox(agent_id)`, `acknowledge(agent_id, idx)` |
| `ctx.meta` | `agents`, `register(agent_id, role)` |

## Spec

All data follows [AContext Spec v1.0](https://github.com/zhaoguoqiang-hub/soul-system/blob/main/spec/context-spec-v1.md).
