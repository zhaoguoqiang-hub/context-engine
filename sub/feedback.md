---
name: feedback-loop
parent: acontext-engine
load: lazy — after any emotionally-toned response
---

# Feedback Loop

Single-character learning signal. Turns blind rules into self-tuning system.

## Detection

After any response where atmosphere mode != task, scan user's NEXT message for leading char:

| Char | Meaning | Action |
|------|---------|--------|
| `+` | mode was right | strengthen: this context→mode mapping +1 |
| `-` | mode was wrong | weaken: switch to neighbor mode, record miss |
| `=` | neutral | no change |

If user message starts with standard Chinese/English text (no leading +-=), skip — no feedback.

## Storage

Append to `feedback.jsonl`:
```json
{"ts":"2026-06-20T10:30","mode":"tender","trigger":"user vented about deadline","result":"-","switch_to":"task"}
```

## Learning

Every 10 entries → compute per-scenario accuracy:

| Mode | Right | Wrong | Accuracy |
|------|-------|-------|----------|

Modes with accuracy < 50% → downgrade to fallback (default task).
Modes with accuracy > 80% → boost confidence, may auto-switch faster.

## Auto-Correction

When `-` received: immediately switch to neighbor mode in next reply.
Don't announce. Just fix.

## Token

feedback-log.jsonl max 100 lines. Oldest rotate out.
