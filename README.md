# AContext

> File-based, user-owned, cross-platform context layer for AI agents.

**AContext** makes your AI agents remember you — across sessions, across platforms, across agents. Like `.git` for agent memory.

```bash
pip install acontext
```

## What it does

| Problem | AContext |
|---------|----------|
| Every agent session starts from zero | Persistent memory across sessions |
| ChatGPT/Claude/Cursor don't share context | One profile, any agent |
| Your agent data is locked in platforms | You own the files. `~/.acontext/` |
| Agents don't know what other agents did | Cross-agent handoff protocol |

## Quickstart

```python
from acontext import AContext
ctx = AContext("~/.acontext")
ctx.profile.update({"preferences": [{"value": "喜欢直接风格", "source": "manual", "added": "2026-06-20"}]})
ctx.narratives.append({"signal": "关键决策", "agent": "codex", "summary": "迁移到Remix"})
```

## Skill (Hermes/Codex)

Add to your `AGENTS.md`:
```markdown
@context-engine/SKILL.md
```

## Spec

[`spec/context-spec-v1.md`](spec/context-spec-v1.md) — language-agnostic. Any agent can implement.

## Structure

```
~/.acontext/          ← your data, your git repo
context-engine/       ← this repo
├── SKILL.md          ← agent skill
├── spec/             ← format specification
├── libs/python/      ← pip install acontext
└── sub/              ← 10 sub-skills
```

## Status

v1.0 — spec stable. Python lib functional. Running on Hermes + Codex.
