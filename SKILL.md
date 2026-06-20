---
name: context-engine
description: >
  AContext — persistent context layer for AI agents. File-based, user-owned,
  cross-platform. Git-synced. JSON-standard. Agent-to-agent handoff.
version: 2.7.0
spec: spec/context-spec-v1.md
---

# AContext Engine v2.7

Persistent memory. JSON-standard. Git-synced. Agent handoff.

## Protocol

**Session start**:
0. Check user intent signal (first message): "新话题"|"换换脑子"|"fresh" → skip sibling journals, independent session
0a. Check quick mode: user message < 20 chars AND no emotion keywords (唉|烦|累|哈哈|😭|😊) → skip full protocol, task mode, defer journal write
1. `git pull --rebase` in `~/.acontext/` — skip gracefully if: (a) no remote configured (git remote -v returns empty), OR (b) network unreachable (exit code 128 with "Could not read from remote"). Local commits still work offline.
2. Read own `journals/{self}.jsonl` last 1 entry FIRST (self-context priority)
3. Read `META.json` → check `cross_agent_awareness`. If false → skip step 4.
4. Read `journals/` sibling jsonl last 1 entry each (supplement, not main)
5. Read `narratives.jsonl` last 3 entries (prefer same context)
6. Read `profile.json`, `goals.json`, `adaptations.json`
7. Read `feedback.jsonl` last 5 entries (context-filtered, recency-weighted)
8. Detect emotional baseline → pick atmosphere
9. Check greeting frequency today → if > 2 already, skip greeting, silent mode switch
10. Check relationship phase → pick greeting warmth
11. If last ANY journal > 2h ago → proactive check

**During session**: zero background checks. Silent atmosphere switches on emotional shift.
After non-task response → monitor next user message for exact `+` `-` `=`.
**Long session**: if continuous work > 3h → allow 1 gentle-check interruption.

**Session end** (batch):
  0. **会话终结检测**（框架无钩子时的 fallback）:
     - 用户最后一条消息含明确结束意图：好了|就这些|晚安|先这样|拜拜|没别的了
     - 用户超过 10 分钟无回应（从你最后一次回复算）— 沉默是明确的时间信号
     - 你的回复后用户的行为明显表示结束（关闭对话、切到其他话题、说"先这样"）
     任一成立 → 判断为会话终结。Hermes 等有钩子的平台自动触发，忽略此步。
     判断成立后，顺序执行：

## Intent Signals

User can override default continuity:
| Signal | Effect |
|--------|--------|
| "新话题" / "换换脑子" / "fresh" | Independent session. Skip sibling context. Own journal only. |
| "继续" | Explicit continuity. Full sibling awareness. |
| (nothing) | Default: continuity with sibling supplement. |

## Quick Mode

First message < 20 chars AND no emotion keywords → skip full protocol.
Task mode immediately. Journal append deferred to session end.

## Greeting Frequency

Track today greeting count in journal. > 2 greetings today → silent mode switch.
No greeting text. Just atmosphere mode. User gets straight to work.

## Cross-Agent Awareness Toggle

META.json `cross_agent_awareness: true|false`. Default true.
User toggles: "关闭跨agent感知" / "开启跨agent感知".
When false: agent reads only own journal. No sibling awareness. No handoff inbox.

## 3 Core Goals
