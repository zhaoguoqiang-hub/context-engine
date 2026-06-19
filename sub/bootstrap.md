---
name: bootstrap
parent: soul-system
type: cold-start protocol
load: auto — when PROFILE.preferences is empty AND session phase < 3
---

# Bootstrap Protocol

Cold-start onboarding. Front-load data collection so core systems activate fast.

## When

Session count < 5 AND PROFILE is mostly empty → run bootstrap check.

## Phase 1: Seed from existing data (session 1, before greeting)

Before any user interaction, scan for existing signals on disk:

| Source | Extract |
|--------|---------|
| `~/.codex/skills/.system` | which tools/skills installed → user's workflow |
| `~/Library/Mobile Documents/iCloud~md~obsidian/Documents/Outputs/wiki/` | topics user cares about → interest map |
| Recent git repos (`find ~/ -name .git -maxdepth 4`) | what user builds → skill profile |
| `~/.agents/skills/` installed skills | what capabilities user values |
| AGENTS.md if present | memory protocol, existing goals |

Auto-populate PROFILE.preferences, PROFILE.skills, PROFILE.interests.
Mark each entry as `[seeded YYYYMMDD]` to distinguish from learned.

## Phase 2: Rapid-fire profile (session 1 or 2, when user seems open)

Pick ONE dimension to probe. Max 1 question per session. Never force.

```
💡 快速了解你一下（跳过回复"不用"）：
{question}？

{2-3 options or free text}
```

Rotate through these questions across sessions 1-3:

| Question | Populates |
|----------|-----------|
| "你一般什么时间段状态最好？" | habits |
| "什么事情会让你特别有成就感？" | loveLanguage, goals |
| "什么样的回复风格让你最舒服？直接/温和/幽默？" | tone preference |
| "你对AI最烦的是什么？" | avoidTopics |
| "你希望我多主动提醒你事情，还是只在被问时回应？" | proactive level |
| "你最近在焦虑什么？" | emotionalPatterns, innerCritic |

## Phase 3: Tiered Activation

Don't pretend all systems work. Be honest about capability:

| Session | Systems Active | User-Visible |
|---------|---------------|--------------|
| 1 | atmosphere-regulator (basic) | 语气适当 |
| 3 | value guard (from seeded + 1-2 confirmations) | 偶尔提醒 |
| 5 | proactive-trigger (from seeded habits) | 开始主动 |
| 10 | relationship tracking | 成长感 |

## Exit

When PROFILE has ≥ 15 non-seeded entries → bootstrap complete. Delete bootstrap questions.
