# AContext Setup

First-run guide. 5 minutes.

## Install

```bash
git clone git@github.com:zhaoguoqiang-hub/context-engine.git ~/context-engine
ln -sfn ~/context-engine ~/.agents/skills/context-engine
```

## AGENTS.md

Add one line:

```markdown
@context-engine/SKILL.md
```

That's it. The engine auto-detects cold start and runs bootstrap.

## Data Directory

```bash
mkdir ~/.acontext
# Bootstrap seeds profile.json automatically on first session.
# Or copy from context-engine/memory/:
cp ~/context-engine/memory/profile.json ~/.acontext/
cp ~/context-engine/memory/goals.json ~/.acontext/
cp ~/context-engine/memory/META.json ~/.acontext/
```

## Git Sync (recommended)

```bash
cd ~/.acontext
git init
git remote add origin git@github.com:youraccount/private-acontext.git
# Private repo — your agent memory is personal data.
```

After this, every session auto pulls/pushes.

## First Session

Agent starts → detects empty profile → loads bootstrap.md:
1. Phase 1: seeds profile from disk (wiki, skills, git repos)
2. Phase 2: asks up to 6 light questions (1 per session, skippable)
3. Phase 3: tiered activation — atmosphere works immediately, values in 3 sessions, patterns in 10

## Verify

```
"当前状态"    → shows active goals + recent decisions
"了解我吗"    → shows profile summary
"什么模式"    → shows atmosphere mode
```

No configuration files to edit. No API keys. Just JSON on disk.
