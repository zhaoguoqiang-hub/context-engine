# Changelog

## v2.6 — 2026-06-20

- Agent handoff protocol (`sub/handoff.md`)
- Profile merge algorithm (field-level timestamp arbitration)
- Cross-agent task chain in narratives
- Proactive trigger updated with handoff inbox

## v2.5 — 2026-06-20

- AContext Spec v1.0 (`spec/context-spec-v1.md`)
- JSON migration: Markdown → JSON/JSONL for all memory files
- Privacy tiers: public / agent:{id} / session
- Handoff envelope format spec

## v2.4 — 2026-06-20

- Git sync layer (`sub/git-sync.md`) — sandbox bridge
- Multi-agent awareness (sibling journal read at session start)
- Agent registry (META.json)

## v2.3 — 2026-06-20

- Feedback loop (`sub/feedback.md`) — `+` `-` `=` learning
- Context compression rules
- Transparency commands: "当前状态", "什么模式", "纠正:..."
- Day-1 value: context brief command

## v2.2 — 2026-06-20

- Atmosphere regulator — 6-mode tone palette
- Emotional attunement — 6 psychology frameworks
- Relationship growth tracking
- Trivia vault + loveLanguage + innerCritic
- Bootstrap protocol for cold start

## v2.1 — 2026-06-19

- Token-light redesign. Lazy-load sub-skills.
- Batch processing at session start/end only.
- Disturbance budget: max 1 proactive/session.

## v2.0 — 2026-06-19

- Pure Skill edition. No plugin needed.
- 5 core sub-skills: mood-simulator, value-aware-guard,
  proactive-trigger, user-context-scanner, narrative-memory.

## v0.1 — 2026-04-01

- Original Plugin-based design (proactive-engine)
- 5 skills + 1 plugin layer
- 6 cron timers + signal loop
