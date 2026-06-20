# AContext

`.git` for agent memory. A file-based context layer that any AI agent reads and
writes — profile, goals, session logs, handoffs. JSON files you own, versioned
with git, shared across Hermes, Codex, Claude Code, or whatever comes next.

```bash
pip install acontext
```

## What you get

Add one line to your agent config:

```markdown
@context-engine/SKILL.md
```

Next session, your agent does this automatically:

```
# session start → git pull (skip if offline)
# read journals → "上次 coding session 做到一半"
# read profile → "Boss喜欢直接风格"
# check goals  → "AContext 开发中 (priority 10)"
```

Session ends, it writes everything back and commits.

```python
from acontext import AContext

ctx = AContext("~/.acontext")
ctx.profile.update({"preferences": [
    {"value": "开门见山", "source": "manual", "added": "2026-06-20"}
]})
```

## Install

```bash
git clone git@github.com:zhaoguoqiang-hub/context-engine.git ~/context-engine
ln -sfn ~/context-engine ~/.agents/skills/context-engine   # or ~/.codex/skills/
```

Then add `@context-engine/SKILL.md` to your `AGENTS.md` or `CLAUDE.md`.

### Data directory (`~/.acontext/`)

```bash
mkdir ~/.acontext && cd ~/.acontext && git init
# optional: add a remote for cross-machine sync
git remote add origin <your-private-repo>
```

Without a remote, local git works fine — pull/push are skipped when offline.

## Directory layout

```
~/.acontext/          ← your data, your git repo
context-engine/       ← this repo
├── SKILL.md          ← agent instructions
├── spec/             ← file format spec (any agent can implement)
├── sub/              ← 10 sub-skills
├── libs/python/      ← pip install acontext
└── memory/           ← seed data
```

## Agent commands

| Say this | Effect |
|----------|--------|
| `"新话题"` / `"fresh"` | 独立会话，不读历史 |
| `"继续"` | 主动延续上下文 |
| `"+"` / `"-"` after reply | 告诉 agent 语气对了还是错了 |
| `"当前状态"` | 当前目标 + 近期决策 |
| `"什么模式"` | 当前 atmosphere 模式 |

## What this isn't

- No server. No database. No cloud.
- No vector embeddings, no RAG, no "AI learning" you can't inspect.
- No lock-in — all files are plain JSON. `cat` and `git log` everything.

## Status

v2.7 — running daily on Hermes + Codex. The spec is stable and agent-agnostic.

[CHANGELOG](CHANGELOG.md) · [Spec](spec/context-spec-v1.md) · [QA Report](references/qa-report.md)
