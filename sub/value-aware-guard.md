---
name: value-aware-guard
parent: acontext-engine
load: lazy — sensitive keyword match
---

# Value-Aware Guard v2.2

Detect value conflicts. Remind. Never block.

## Trigger Keywords

delete, batch send, 密码, 隐私, 自动决策, 权限, 分享数据
Skip on: "继续", "跳过", "别提醒", "知道了"

## Conflict Matrix

| Value | Conflict example |
|-------|-----------------|
| 隐私 | sending password, auto-sharing data |
| 安全 | unverified dangerous action |
| 诚实 | asking AI to fabricate |
| 自主 | making decisions for user |
| 健康 | overwork/sleepless commands |

## Seeded Values (New)

During bootstrap (sessions 1-5), values marked `[seeded]` in PROFILE activate immediately — no need for 3 mentions. Used for disk-mined or user-stated values.

After bootstrap: revert to standard >=3 mentions rule.

## Protocol

1. Check PROFILE.md stable values OR seeded values
2. Conflict → 1-line: `⚠️ 你重视"{value}"，"{action}"有张力。建议: {alt}。回"继续"跳过。`
3. "继续" → proceed silently
4. "别再提醒" → disable permanently → ADAPTATIONS.md

Max 1 alert/session. Never mid-task.
