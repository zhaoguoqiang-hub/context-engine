---
name: handoff
parent: context-engine
load: lazy — session end (write) AND session start (read inbox)
---

# Agent Handoff Protocol

Agent-to-agent structured handoff. Not a note — a contract.

## Significant Task — Definition (v2.7.3)

A task is "significant" when it meets **any one** of:

| # | Condition | Example |
|---|-----------|---------|
| a | 用户明确说"完成" + 任务名 | "X部署完成了" |
| b | 部署/发布/merge 操作 | git push, npm publish, docker push |
| c | 创建了新文件/项目 | 新 repo, 新 skill, 关键文档 |
| d | 单会话连续工作 > 2h | 长 session 结束时自动标记 |
| e | 任何涉及 **文件系统写 + 跨 agent** 的操作 | 写了 `~/Output/` 下的内容 |

**不定义**为 significant：
- 纯查询/搜索/阅读
- 单 agent 内部运维（journal、profile 更新）
- 用户说"不相关"/"不用告诉另一个"

## Write (session end, after significant task)

When agent completes a task that another agent should know about,
write to `handoffs/{target_agent}.json`:

```json
{
  "_meta": {"v":"1.0"},
  "from": "{self}",
  "to": "hermes",
  "ts": "2026-06-20T15:30:00+08:00",
  "completed": ["deployed user-service to staging"],
  "pending": ["integration tests not yet run", "monitoring dashboard pending"],
  "needs": ["hermes deployment pipeline", "cron job setup"],
  "files": ["infra/deploy.sh", "infra/.env.staging"],
  "notes": "DB migrations applied. Rollback tested. Health check endpoint at /healthz.",
  "acknowledged": false
}
```

## Read (session start)

Check `handoffs/{self}.json`:
- If `acknowledged: false` → new handoff. Read, act, acknowledge.
- If `acknowledged: true` → already processed, skip.

## Acknowledge

After processing handoff, set `acknowledged: true` and add `acknowledged_ts`.

## Cross-Agent Task Chain

When processing handoff → signal "关键决策" to narratives.jsonl with `tags:["#交接","#跨agent"]`.
Links tasks across agent boundaries in shared timeline.

## Profile Merge

When two agents independently update profile.json → git merge conflict possible.
Resolution:
1. Compare `_meta.updated` timestamps per field
2. Newer field wins for conflicting fields
3. Merge non-conflicting fields from both versions
4. Append `_meta.merge_log` entry: `{"ts":"ISO","merged_from":["agentA","agentB"],"conflicts":["preferences.0"]}`

## Bugfix (v2.7.1)

acknowledge with out-of-range index → silently ignore (no crash).
