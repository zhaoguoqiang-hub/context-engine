# Context Memory Compression

Long-running system. Data grows. Must compress or die.

## Compression Triggers

Run at session end every 10th session.

## Compression Rules

| File | Threshold | Action |
|------|-----------|--------|
| PROFILE entries | 90d unused | archive to `memory/archive/profile-YYYYMM.md`, remove from active |
| NARRATIVES events | > 180d old | compress all old events into 1 summary paragraph at top |
| journals/*.md | entries > 30d | compress to 1 line: `YYMMDD | mood | done_summary` |
| feedback-log.jsonl | > 100 lines | delete oldest 20 |
| REFLECTIONS | insights > 90d | compress to 1 line each |

## PROFILE entry "used" definition

An entry is "used" when:
- Referenced in last 30 days' journals
- Mentioned in last 30 days' NARRATIVES
- user-context-scanner updated it in last 90 days

## NARRATIVES compression format

Replace all entries older than 180d with:
```
## YYYY上/下半年 摘要

{1 paragraph weaving key decisions, milestones, emotional arcs}
```
