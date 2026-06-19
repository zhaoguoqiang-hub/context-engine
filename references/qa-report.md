# QA Report — AContext v2.7

## P1 — 会导致错误行为

### BUG-01 问候规则缺少 06:00-08:00 时段

**位置**：SKILL.md Greeting Rules 表

时间覆盖：08:00-12:00 / 12:00-18:00 / 18:00-22:00 / 22:00-06:00。06:00-08:00 缺失。用户 7:00 启动 → 无匹配规则 → greeting 未定义。

**修**：补 `06:00-08:00` → "早。今天有什么计划？"（同 first session）

### BUG-02 "首次会话"判断不适用连续场景

**复现**：用户 07:00-10:00 在 Hermes 工作 → 10:01 切到 OpenClaw。sibling journal 显示 3h 活动 → 走 continuity 规则，正确。但如果用户 07:00-07:30 在 Hermes 做了 30 分钟 → 8:00 切到 OpenClaw → sibling 50 分钟前活动 → 走 "active work in last 1h" → 说"刚忙完"——但实际是用户吃了早饭回来开始新工作。

**根因**：只检查了 sibling 最后活动时间，没检查时间间隔的模式——连续工作 vs 工作-休息-新工作。

**修**：增加判断——如果 sibling 最后 mood 是 task 且最后活动 < 30min → 连续。否则即使 < 1h 也可能是新 session。

### BUG-03 PROFILE 损坏无容错

**复现**：profile.json 损坏（手动编辑出错 / 磁盘错误 / 两个 agent 同时写）。`read()` 返回 `_empty()`，所有积累数据丢失，且无恢复机制。

**根因**：`ProfileManager.read()` 没有 try/catch。JSON 解析失败不返回空，直接抛异常。

**修**：(1) Python 库 `json.loads` 包 try/catch。解析失败 → 从 `.bak` 恢复。(2) 原子写入时同时写 `.bak` 副本。

### BUG-04 反馈检测误匹配 "++" "+1" "+ 不错"

**复现**：用户回复 "+1 这个方案好"。系统检测到首个字符是 `+` → 当成正向反馈。但 "+1" 可能是"我同意你说的方案"而不是"语气对了"。"++" 同理。

**根因**：反馈检测只看首字符，没有上下文。

**修**：精确匹配——仅当消息**恰好是** `+` / `-` / `=` 或**以这些字符开头且后跟空格或换行**才触发。`+1`、`++`、`+不错` 不触发。

### BUG-05 PROACTIVE 触发器未考虑 sibling journal

**复现**：用户的 OpenClaw 昨天用过（journal > 24h）。今天在 Hermes 工作了 3 小时。切到 OpenClaw → proactive check 看自己的 journal > 2h → 是 → 触发主动建议。但用户已经工作了 3 小时，立即收到"要不要做 X"的建议是打断。

**根因**：proactive check 只看自己的 journal。

**修**：proactive check 看所有 journal 的最后活动时间。取最近的那条。

---

## P2 — 体验退化

### BUG-06 "重大任务"触发交接——未定义

**位置**：SKILL.md Session End step 5

"if significant task completed → write handoff"。什么是 significant？未定义。Agent 要么从不写 handoff，要么什么都写。

**修**：定义 significant = 满足以下任一：(a) 用户说"完成" + 任务名，(b) 部署/发布/merge 操作，(c) 创建了新文件/项目，(d) 单会话连续工作 > 2h。

### BUG-07 Bootstrap Phase 2 无限跳过

**复现**：用户每次都说"不用"/"跳过"。6 个问题全跳过。Phase 2 永远不完成。Bootstrap exit 永远达不到。

**修**：3 次跳过后 → Phase 2 自动结束。标记 `bootstrap_phase2_skipped: true`。

### BUG-08 反馈准确率冷启动除以零

**复现**：新系统 feedback.jsonl 为空。计算准确率 → 0/0。无法判断是否该降级到 task。

**修**：< 5 条反馈 → 不计算准确率。使用默认权重（所有模式等权）。

### BUG-09 多 sibling 活动时取哪条

**复现**：hermes + codex 同时有最近活动。hermes mood=tender, codex mood=task。OpenClaw 启动 → 取哪条作为 continuity 依据？

**修**：取时间最近的那条。如果两条时间相同（< 1min 差异）→ 取 mood 最接近自己默认的。

### BUG-10 压缩删除最后一条 narrative

**复现**：刚好 1 条 narrative 且它 > 180 天。压缩 → 删掉 → narratives.jsonl 为空。下次 `last(3)` 返回空。

**修**：压缩后至少保留最近 1 条，无论年龄。

---

## P3 — 边界情况

### BUG-11 Context 搜索全空时无兜底

narratives `search(context="coding")` 返回 0 条 → 静默返回空。Agent 无上下文。应该 fallback 到 universal。

### BUG-12 Handoff acknowledge 越界

`acknowledge("hermes", 5)` 但 inbox 只有 2 条 → 应该静默忽略而不是抛异常。

### BUG-13 用户说"专注模式"无截止时间

专注模式永久激活，用户可能忘记关闭。应默认 2h 自动恢复。

### BUG-14 Sibling journal 时间戳跨时区比较

hermes 用 UTC，codex 用 +08:00。`ts` 字段直接字符串比较会错。应统一解析为 datetime 再比较。

---

## 测试矩阵

| 场景 | 覆盖 |
|------|------|
| 单 agent 首发 | bootstrap → seed → Phase 2 questions |
| 双 agent 连续工作 | continuity greeting → atmosphere bias |
| 三 agent 同时活动 | 多 sibling 取最近 |
| 数据损坏 | profile.json corrupted → recovery |
| 空数据 | feedback.jsonl 0 entries → default weights |
| 超大文件 | narratives.jsonl 5000 条 → last() 性能 |
| 网络断线 | git pull/push 失败 → 不阻断 |
| 跨时区 | UTC/+08:00 timestamp 比较 |
