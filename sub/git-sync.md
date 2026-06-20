---
name: git-sync
parent: context-engine
load: lazy — session start/end
---

# Git Sync

git repo as sandbox bridge. Push deferred to session start — zero OS dependency.

## 部署模式

| 模式 | 检测 | 行为 |
|------|------|------|
| 本地 | 无 remote | journal写作写完，git commit，不push |
| 跨设备 | 有 remote | start时push+pull，end时commit |
| 日备份 | 每天首次启动 | 有remote则额外push一次 |

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

## Critical: Never Remove Remote

**Never delete or modify `git remote` programmatically.** Invalid remote → push fails gracefully (no output, exit silently). Data stays local.

如果 remote 指向不存在的仓库，换 URL 即可，不要删除：

```bash
cd ~/.acontext && git remote set-url origin git@github.com:youraccount/正确的仓库.git
```

Without remote, other machines cannot sync. Local mode still works but cross-device sync and daily backup are disabled.
