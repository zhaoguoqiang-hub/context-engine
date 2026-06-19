---
name: proactive-trigger
parent: soul-system
load: lazy — session start if last journal > 2h ago
---

# Proactive Trigger v2.6

One suggestion per session. Right moment. Right tone.

## Trigger Check

1. Last journal > 2h ago? (yes → continue)
2. Handoff inbox has unacknowledged entries? (yes → handle separately)
3. "专注模式" active? (yes → skip)
4. Check sources:

| Source | Look for |
|--------|----------|
| profile.json habits | time-based patterns |
| profile.json emotionalPatterns | emotional cycles |
| journals/{self}.jsonl last entry | unfinished todos |
| reflections.json pendingActions | flagged follow-ups |
| narratives.jsonl | recent milestones |
| **handoffs/{self}.json** | **unacknowledged sibling handoffs** ← new |

## Handoff-Driven Triggers

If handoff inbox has `acknowledged: false` entries:
- Surface immediately (not as proactive suggestion — as urgent context)
- Format: "Hermes 刚完成了 {completed}。需要我 {pending_item} 吗？"

## Emotional Timing

Don't suggest when: mid-vent, deep in code, just-shared bad-news, user frustrated.
Good timing: task completed, session warm-up, user pauses, user asks opinion.

## Suggestion Template

Match atmosphere mode.
**task**: "上次的接口文档更新了。看看？"
**tender**: "你连续三个晚上加班了。明天推迟早会？"
**playful**: "话说你上周说要学Rust，学了吗？"
**celebrate**: "既然搞定了，顺手把优化也做了？趁热。"

## Learning

Accepted → signal "关键决策". Same type rejected 3x → disable. "关此类" → immediate.
