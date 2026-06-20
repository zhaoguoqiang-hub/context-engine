---
name: git-sync
parent: soul-system
load: lazy — session start/end
---

# Git Sync

git repo as sandbox bridge. File-based + user-owned + cross-agent.

## Setup (one-time)

```bash
# Create private repo on GitHub: youraccount/acontext
cd ~
git clone git@github.com:youraccount/acontext.git .acontext
# Copy existing soul-system memory files in:
cp ~/.agents/skills/soul-system/memory/*.jsonl .acontext/
cp ~/.agents/skills/soul-system/memory/*.json .acontext/
cp -r ~/.agents/skills/soul-system/memory/journals .acontext/
cd .acontext && git add -A && git commit -m "init acontext" && git push
```

## Session Start

```bash
cd ~/.acontext && git push -q 2>/dev/null && git pull --rebase 2>/dev/null || true
```

```bash
cd ~/.acontext && git pull --rebase 2>/dev/null || true
```

Failure → work with local data. Not blocking.

## Session End (keep existing, add note)

Commit only. Push deferred to next session start.

```bash
cd ~/.acontext
git add -A
git commit -m "agent:{self} {YYYYMMDD} {HH:MM}" --allow-empty
git push 2>/dev/null || echo "push failed, saved locally"
```

Push failure → retry next session. Data safe locally.

## Conflict Resolution

Only `profile.json` can conflict (two agents update same field):

1. Read both timestamps from `_meta.updated` field
2. Newer wins for that field
3. Merge non-conflicting fields from both
4. Append `_meta.conflicts` note if needed

All other files are append-only → zero conflict by design.

## When to Enable

After Phase 1 complete (JSON migration done). Currently memory files are mixed Markdown.
Skip git sync until spec migration complete.

## Token

Shell commands only. No token consumption beyond this file load.
