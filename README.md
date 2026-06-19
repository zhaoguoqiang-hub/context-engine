# AContext

> File-based, user-owned, cross-platform context layer for AI agents.

Makes your AI agents remember you — across sessions, platforms, and agents. Like `.git` for agent memory.

```bash
pip install acontext
```

## What it does

| Problem | AContext |
|---------|----------|
| Every agent session starts from zero | Persistent memory across sessions |
| ChatGPT/Claude/Cursor don't share context | One profile, any agent |
| Your agent data is locked in platforms | You own the files. `~/.acontext/` |
| Agents don't know what other agents did | Cross-agent handoff + continuity |
| AI tone feels wrong for the moment | 6-mode atmosphere engine with feedback learning |
| Switching agents mid-workflow loses context | Intent signals, quick mode, greeting fatigue awareness |

## Quickstart

```python
from acontext import AContext
ctx = AContext("~/.acontext")
ctx.profile.update({"preferences": [{"value": "喜欢直接风格", "source": "manual", "added": "2026-06-20"}]})
ctx.narratives.append({"signal": "关键决策", "agent": "codex", "context": "coding", "summary": "迁移到Remix"})
```

## Agent Skill

Add to your `AGENTS.md` / `CLAUDE.md`:

```markdown
@context-engine/SKILL.md
```

Works with Hermes, Codex, Claude Code, OpenClaw — any agent with filesystem access.

## Platforms

| Agent | Config | Install |
|-------|--------|---------|
| Hermes Agent | `AGENTS.md` | symlink to `~/.agents/skills/context-engine/` |
| Codex | `AGENTS.md` | symlink to `~/.codex/skills/context-engine/` |
| Claude Code | `CLAUDE.md` | symlink to `~/.claude/skills/context-engine/` |
| OpenClaw | `AGENTS.md` | symlink to `~/.openclaw/workspace/skills/context-engine/` |

## Highlights

- **Intent signals** — say "新话题" to start fresh, "继续" for explicit continuity
- **Quick mode** — short messages skip protocol overhead
- **6 atmosphere modes** — task / playful / tender / celebrate / gentle-check / reflective
- **Feedback learning** — `+` / `-` trains tone accuracy per context
- **Context-aware memory** — coding memories don't pollute creative sessions
- **Recency-weighted** — old feedback decays, recent matters more
- **Self-first** — own session context before sibling awareness
- **Cross-agent toggle** — turn off sibling awareness when you want privacy

## Spec

[`spec/context-spec-v1.md`](spec/context-spec-v1.md) — language-agnostic. Any agent can implement.

## Structure

```
~/.acontext/          ← your data, your git repo
context-engine/       ← this repo
├── SKILL.md          ← agent skill (62 lines)
├── spec/             ← format specification
├── sub/              ← 10 sub-skills
├── libs/python/      ← pip install acontext
├── memory/           ← JSON seed data
└── references/       ← QA report, UX review, philosophy, competitive analysis
```

## Status

v2.7.2 — 14 bugs fixed, 6 UX improvements. QA tested. Running on Hermes + Codex. OpenClaw/Claude Code ready.

[CHANGELOG](CHANGELOG.md) · [QA Report](references/qa-report.md) · [UX Review](references/ux-review.md)
