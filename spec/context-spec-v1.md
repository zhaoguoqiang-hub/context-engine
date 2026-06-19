# AContext Spec v1.0

Agent Context open standard. File-based, user-owned, cross-platform.

## Directory Layout

```
~/.acontext/
├── META.json                    # Agent registry
├── profile.json                 # User identity
├── goals.json                   # Core goals
├── adaptations.json             # Behavioral rules
├── narratives.jsonl             # Shared timeline (append-only)
├── reflections.json             # Long-term insights
├── feedback.jsonl               # Learning signals
├── journals/{agent_id}.jsonl    # Per-agent session logs
├── handoffs/{agent_id}.json     # Agent-to-agent handoff
├── archive/                     # Compressed old data
└── spec.md                      # This spec (optional, for reference)
```

## Privacy Tiers

Every entry MUST include a `privacy` field:

| Tier | Value | Scope |
|------|-------|-------|
| Public | `"public"` | All registered agents |
| Agent-only | `"agent:{id}"` | Only specified agent |
| Ephemeral | `"session"` | Delete after session end |

## profile.json

```json
{
  "_meta": {"v": "1.0", "updated": "2026-06-20T10:00:00+08:00"},
  "preferences": [{"value":"喜欢用Obsidian","source":"session_20260620","added":"2026-06-20"}],
  "habits": [{"pattern":"晚上10点后写作","confidence":2,"source":"seeded_20260620"}],
  "values": {
    "stable": [{"value":"隐私","mentions":3,"first_seen":"2026-06-15"}],
    "potential": [{"value":"效率","mentions":1,"first_seen":"2026-06-20"}]
  },
  "trivia": [{"detail":"夏天只喝冰美式","source":"session_20260620"}],
  "humorStyle": "",
  "emotionalPatterns": [{"pattern":"截稿日前易焦虑","occurrences":0,"confidence":0}],
  "loveLanguage": "",
  "innerCritic": [],
  "avoidTopics": [],
  "skills": [{"name":"Python","level":"expert","source":"seeded_20260620"}],
  "goals": []
}
```

## goals.json

```json
{
  "_meta": {"v": "1.0", "updated": "2026-06-20T10:00:00+08:00"},
  "goals": [
    {"id":"core-1","name":"用户长期福祉","priority":10,"status":"active","progress":0,"keywords":["熬夜","通宵","不吃饭","过度"]},
    {"id":"core-3","name":"维护信任关系","priority":9,"status":"active","progress":0,"keywords":["隐私","密码","诚实","透明"]},
    {"id":"core-2","name":"持续自我优化","priority":8,"status":"active","progress":0,"keywords":["反馈","纠正","改进"]}
  ]
}
```

## adaptations.json

```json
{
  "_meta": {"v": "1.0", "updated": "2026-06-20T10:00:00+08:00"},
  "active_rules": [],
  "disabled_rules": [],
  "session_rules": []
}
```

## narratives.jsonl (append-only)

```jsonl
{"ts":"2026-06-20T10:30:00+08:00","signal":"关键决策","agent":"codex","summary":"用户决定从Next.js迁移到Remix","context":"比较两个框架后选择Remix","impact":"后续开发基于Remix","tags":["#决策","#技术选型"],"privacy":"public"}
```

## feedback.jsonl (append-only)

```jsonl
{"ts":"2026-06-20T10:30:00+08:00","agent":"codex","mode":"tender","trigger":"user vented about deadline","result":"+","switch_to":null}
```

## journals/{agent_id}.jsonl (append-only)

```jsonl
{"ts":"2026-06-20T10:30:00+08:00","agent":"codex","mood":"task","work":["完成了X","做了Y"],"emotional_moments":["用户提到截稿压力"],"patterns":["深夜工作效率更高"],"profile_updates":["新增偏好:喜欢直接风格"],"todos":["跟进接口文档"]}
```

## handoffs/{agent_id}.json

```json
{
  "_meta": {"v": "1.0"},
  "from": "codex",
  "to": "hermes",
  "ts": "2026-06-20T10:30:00+08:00",
  "completed": ["部署了API服务到staging"],
  "pending": ["需要跑集成测试"],
  "needs": ["Hermes的自动化部署能力"],
  "files": ["/path/to/deploy.sh"],
  "notes": "环境变量在.env.staging。数据库迁移已跑完。",
  "acknowledged": false
}
```

## META.json

```json
{
  "_meta": {"v": "1.0", "updated": "2026-06-20T10:00:00+08:00"},
  "agents": {
    "hermes": {"id":"hermes","role":"任务自动化+三省六部","active":true},
    "codex": {"id":"codex","role":"开发+深度分析","active":true}
  }
}
```

## reflections.json

```json
{
  "_meta": {"v": "1.0", "updated": "2026-06-20T10:00:00+08:00"},
  "weekly_insights": [],
  "pending_actions": [],
  "archive": []
}
```

## v1.1 Additions (context + temporality)

### context field (all entry types)
- NarrativeEvent, JournalEntry, FeedbackEntry, ProfileEntry: add `context` field
- Values: `"coding"` | `"creative"` | `"research"` | `"life"` | `"universal"`
- Load logic: prefer same-context entries, fallback to universal

### recency_weight (FeedbackEntry)
- Formula: `max(0.1, 1.0 - days_since / 30)`
- Accuracy computed over last 50 entries, weighted by recency
- Per (context, mode) grouping

### expires (ProfileEntry)
- ISO date or null. null = permanent.
- Conflict resolution: context-specific > universal. Newer timestamp wins for same context.
