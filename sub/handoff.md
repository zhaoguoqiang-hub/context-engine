---
name: handoff
parent: context-engine
load: lazy — session end (write) AND session start (read inbox)
---

# Agent Handoff Protocol

Agent-to-agent structured handoff. Not a note — a contract.

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
