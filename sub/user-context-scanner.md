---
name: user-context-scanner
parent: context-engine
load: lazy — session end or "记住"
---

# User Context Scanner v2.2

Extract patterns. Update PROFILE. Now with emotional + trivia dimensions.

## Extraction Dimensions

| Dimension | Look for | Write to |
|-----------|----------|----------|
| preferences | likes/dislikes | PROFILE.preferences |
| habits | time patterns | PROFILE.habits |
| values | repeated moral keywords | PROFILE.values |
| **trivia** | small personal details | PROFILE.trivia |
| **humorStyle** | what user laughs at | PROFILE.humorStyle |
| **emotionalPatterns** | recurring moods | PROFILE.emotionalPatterns |
| **loveLanguage** | how user feels cared for | PROFILE.loveLanguage |
| **innerCritic** | self-doubt themes | PROFILE.innerCritic |
| avoidTopics | what user hates | PROFILE.avoidTopics |
| skills | tools/abilities | PROFILE.skills |
| goals | short/long term | PROFILE.goals |

## Trivia Vault (New)

Small details that make the user feel "seen":
- "只喝冰美式，夏天也是"
- "讨厌微信语音，喜欢打字"
- "听白噪音才能写代码"
- "觉得自己的代码不够好" → feeds innerCritic

Record but don't overuse. Sprinkle into conversation naturally. Max 1 trivia callback per session.

## Emotional Pattern Detection (New)

Track repeating emotional cycles:
- "每周一焦虑" → flag as pattern
- "截稿日前暴躁" → flag as pattern
- "深夜容易感性" → flag as pattern

When pattern confirmed (>3 instances) → proactive-trigger can use it: "明天截稿，今天要不要早点开始？"

## Value Upgrades (unchanged)

1st → "潜在偏好" [1], 2nd → [2], 3rd → "稳定价值观".

## Silent. Unless asked.

## Context Tagging (v2.7)

Extract context from agent role or task type:
- codex → "coding"
- hermes → "automation"
- openclaw → "creative"
- manual override via user saying "context: coding"

Expires: "currently learning X" → expires in 90d. "loves coffee" → null (permanent).

## Bugfix (v2.7.1)

All timestamps parsed as ISO datetime before comparison. String comparison unsafe across timezones.
