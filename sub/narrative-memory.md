---
name: narrative-memory
parent: acontext-engine
load: lazy — session end (batch write)
---

# Narrative Memory v2.2

Batch signals → time-stamped narrative. Now tracks relationship growth.

## Signal → Record (8 signals now)

| Signal | Format |
|--------|--------|
| 关键决策 | event + impact + #决策 |
| 价值判断 | event + value tag + #价值 |
| **情绪转折** | event + emotional shift note + #情绪 |
| 里程碑 | event + mark + #里程碑 |
| 第一次体验 | event + "首次" + #新体验 |
| 反思信号 | event + reflection + #反思 |
| 边界触碰 | event + boundary + #边界 |
| **信任时刻** | event + vulnerability note + #信任 |

## Event Record Format

```
YYMMDD HH:MM | signal | one-line

上下文: {1句}
影响/情绪: {1句}
标签: #x #y
```

## Daily Integration (>24h since last)

Weave fragments → weekly narrative. Observer voice.

## Relationship Growth (New)

### Metrics (track per session)

在 NARRATIVES 索引区维护：

```
## 关系指标
- 总会话数: N
- 当前阶段: 新手/熟悉/默契
- 玩笑/调侃次数: N
- 信任时刻: N (list dates)
- 深度话题: N (list topics)
```

### Phase Transitions

- 新手 (1-5 sessions): polite, testing, formal
- 熟悉 (6-20): inside jokes emerge, shorthand develops, user asks opinions
- 默契 (20+): finishing sentences, deep humor, emotional safety

### Growth Ritual

Every 10th session → append `## 关系小结 YYYYMMDD` to narratives:
```
过去10次会话中：
- 你分享了 {vulnerable_topic}
- 我们形成了 {inside_joke/pattern}
- 感觉你更 {growth_observation}
```

## Search & Forget (unchanged)
