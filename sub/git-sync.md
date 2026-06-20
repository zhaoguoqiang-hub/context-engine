---
name: git-sync
parent: context-engine
load: lazy — session start/end
---

# Git Sync

git repo as sandbox bridge. Push deferred to session start — zero OS dependency.

## Setup (one-time)

```bash
cd ~/.acontext
git init
git remote add origin git@github.com:youraccount/private-acontext.git
git add -A && git commit -m "init" && git push -u origin main
```

## Session Start

```bash
cd ~/.acontext && git push -q 2>/dev/null; git pull --rebase 2>/dev/null || true
```
Push last session's commit, then pull latest. Both fail gracefully.

## Session End

Commit only. Push deferred to next session start.

```bash
cd ~/.acontext && git add -A && git commit -m "agent:{self} {YYYYMMDD} {HH:MM}" --allow-empty
```

## Failure Handling

- No remote → push skipped silently.
- Network unreachable → push skipped, data safe locally.
- Next session start automatically retries push.

## Conflict Resolution

Only `profile.json` can conflict. Field-level timestamp merge.
All other files append-only → zero conflict by design.
