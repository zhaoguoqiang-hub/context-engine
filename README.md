# AContext

**`.git` for agent memory.** A directory on your machine that every AI agent
reads and writes — profile, goals, session logs, handoffs. JSON files you own,
versioned with git, shared across Hermes, Codex, Claude Code, or whatever comes
next.

```bash
pip install acontext
```

## The short version

Every time you switch between agents — or start a new session — the agent pulls
your context from `~/.acontext/`, reads what happened last time, and picks up
where you left off. No more "Hi, how can I help you today?" five times a day.

It's just files. You can `cat` everything. You can `git log` everything. You
can `cp -r ~/.acontext` to a new machine and be done.

## How it works

An agent that has AContext wired in will, at session start:

1. `git pull --rebase` your context directory (or skip if you're offline)
2. Read its own journal — what did we do last session?
3. Optionally read sibling journals — what did Codex do while Hermes was idle?
4. Load your profile, active goals, learned rules
5. Check the tone — task mode, playful, reflective, etc.
6. Decide if it should greet you or just shut up and get to work

At session end, it writes everything back as structured JSON and commits.

```python
from acontext import AContext

ctx = AContext("~/.acontext")
ctx.profile.update({"preferences": [
    {"value": "开门见山", "source": "manual", "added": "2026-06-20"}
]})
ctx.narratives.append({
    "signal": "关键决策", "agent": "codex",
    "summary": "迁移到Remix"
})
```

## Why not just use the agent's built-in memory?

Because it's locked in that agent. Switch from ChatGPT to Claude Code and your
memory is gone. AContext is a file. You own it. Any agent with filesystem access
can read it.

Also, most "memory" systems are black boxes. You can't inspect them, edit them,
or back them up. AContext is JSON + git. If you can use `cat` and `git`, you
have full control.

## Who's this for

People who run multiple AI agents and want them to feel like the same assistant.
People who care about owning their data. People who've been burned by "we'll
remember that" and then it doesn't.

Currently tested on Hermes Agent and Codex. The spec is agent-agnostic.

## Project layout

```
~/.acontext/          ← your data, your git repo
context-engine/       ← this repo
├── SKILL.md          ← agent integration instructions
├── spec/             ← the file format spec (anyone can implement)
├── sub/              ← 10 sub-skills (atmos, handoff, feedback, etc.)
├── libs/python/      ← pip install acontext
├── memory/           ← seed data to get started
└── references/       ← QA report, UX review, etc.
```

## Quick start (agent setup)

Add one line to your `AGENTS.md` / `CLAUDE.md`:

```markdown
@context-engine/SKILL.md
```

Then symlink the skill:

```bash
git clone git@github.com:zhaoguoqiang-hub/context-engine.git ~/context-engine
ln -sfn ~/context-engine ~/.agents/skills/context-engine
```

That's it. Next session, the agent runs the protocol.

### If you want cross-machine sync

```bash
cd ~/.acontext
git remote add origin <your-private-repo-url>
```

Without a remote, everything works locally — you just won't sync across
machines. Git pull/push are skipped gracefully when there's no network.

## What you can tell your agent

| Say this | It does |
|----------|---------|
| "新话题" / "fresh" | Fresh session, skip past context |
| "继续" | Explicit continuity |
| "+" / "-" after reply | Tells the agent the tone was right or wrong |
| "当前状态" | Shows active goals + recent decisions |
| "什么模式" | Shows current atmosphere mode |

## Anti-features (what it doesn't do)

- No server. No database. No cloud dependency.
- No vector embeddings. No RAG. No LLM calls on your context data.
- No automatic "learning" that you can't see, edit, or delete.
- No lock-in. All files are standard JSON.

## Status

v2.7 — running daily on Hermes + Codex. The spec is stable. The library is
usable. Feedback loop, atmosphere engine, handoff protocol, and git sync have
been through real-world use.

[CHANGELOG](CHANGELOG.md) · [Spec](spec/context-spec-v1.md) · [QA Report](references/qa-report.md)
