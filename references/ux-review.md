# UX Review — AContext v2.7.1

## 场景遍历

### 场景 1：正常工作日上午切换 ✅

08:00 Hermes 启动 → "早。今天有什么计划？" → 工作 2h
10:00 切 Codex → sibling Hermes 1h 内 activity, mood=task
→ "Hermes 刚忙了 2 小时。现在有什么要接手的？"

**评分**：✅ 正确。连续工作，自然过渡。

### 场景 2：切换是为了换脑子 ❌

14:00-16:00 Codex 调试 → 挫败、mood=tender
16:01 切 OpenClaw → 想写小说放松
→ 读 sibling：Codex mood=tender → bias toward tender
→ Greeting："Codex 刚忙了 2 小时。现在有什么要接手的？"

用户心理：**我是来逃离写代码的，不想被提醒刚才在写代码。**

**评分**：❌ 气氛假设用户情绪延续——但用户切换 agent 可能恰恰是为了改变状态。

### 场景 3：长会话零关怀 ❌

09:00-14:00 Codex 连续工作 5h。系统设计：零 mid-session 检查。
用户连续 5 小时没休息——agent 完全不知道，因为它"不打断"。

但连续工作 5 小时恰恰是需要打断的场景。

**评分**：❌ "零打扰"的代价是——真正需要打扰的时候也不打扰。

### 场景 4：频繁切换的问候疲劳 ❌

一天切换 6 次 agent。每次都是：
→ git pull → 读 sibling → 分析 mood → 生成 greeting
第 4 次切过去，用户只想敲命令。greeting 从"贴心"变成"啰嗦"。

**评分**：❌ greeting 没有频率感知。不知道用户今天已经被问候过 3 次了。

### 场景 5：被遗忘的 agent 失去自我 ❌

OpenClaw 2 周没用。启动时：
→ sibling journals 显示最近 activity → continuity greeting
→ 但 OpenClaw 自己的 journal 是 2 周前的
→ 它不知道上次在 OpenClaw 上做什么——"自己的记忆"丢了

**评分**：❌ agent 自己的 last session context 被 sibling activity 淹没。

### 场景 6：跨 agent 感知的"毛骨悚然" ❌

用户 3 个 agent 来回切换一天。每个 agent 都说"XX 刚做了 Y"。
到晚上用户想：它们是不是在背后聊我？

跨 agent 感知是功能——但需要开关。不是每个人都想 agent 互相知道。

**评分**：❌ 默认开启，无关闭方式。

### 场景 7：30 秒小任务触发完整协议 ❌

打开 Codex → 只想问"这个函数签名是什么？" → 30 秒的事。
但 agent 执行了完整的 session start：git pull → 读 5 个文件 → 算气氛 → 查 proactive。

**评分**：❌ 没有"快速模式"。小任务不值得启动全引擎。

---

## 评级汇总

| 场景 | 主动性 | 跨 agent 切换 | 综合 |
|------|--------|-------------|------|
| 1. 正常上午切换 | ✅ | ✅ | ✅ |
| 2. 切 agent 换脑子 | ❌ | ❌ | ❌ |
| 3. 长会话零关怀 | ❌ | N/A | ❌ |
| 4. 频繁切换疲劳 | ⚠️ | ❌ | ❌ |
| 5. 遗忘 agent 迷失 | ⚠️ | ❌ | ❌ |
| 6. 毛骨悚然 | N/A | ❌ | ❌ |
| 7. 小任务大开销 | ❌ | N/A | ❌ |

**7 个场景，1 个通过，6 个失败。**

---

## 根因分析

问题不是"功能缺失"。是设计假设错了：

**假设 1**：切换 agent = 继续工作。→ 实际：切换可能意味着改变状态。
**假设 2**：零打扰 = 好体验。→ 实际：有些打扰是关怀，有些沉默是冷漠。
**假设 3**：知道越多越好。→ 实际：知道多少和展示多少是两回事。
**假设 4**：全协议每次执行。→ 实际：小任务不需要 5 个文件读取。

---

## UX 改进提案

### 1. 意图信号——用户告诉 agent 为什么切过来

启动时加一个轻量意图：
- 用户什么都不说 → 默认 continuity（当前行为）
- 用户说"新话题" / "换换脑子" → 跳过 sibling 上下文，独立 session
- 用户说"继续" → 显式确认连续性

一句 2 个字。零负担。解决场景 2、6。

### 2. 长会话软中断

连续 > 3h 工作 → 允许 1 次 gentle-check。
不是 proactive suggestion——是关怀。"三个小时了。眼睛歇一下？"

与当前的"零 mid-session"原则的冲突：把"不打扰"改成"只在值得打扰时打扰"。

### 3. 问候频率感知

记录今天已经被问候过的次数（在 journal 里）。> 2 次 → 问候降级为静默模式切换。不说话了，直接进入 task。

### 4. 快速模式

消息 < 20 字 AND 不含情绪词 → 跳过全协议。直接 task 模式回复。session end 才补写 journal。

### 5. 跨 agent 感知开关

META.json 加 `cross_agent_awareness: true|false`。关闭后，agent 只读自己的 journal。不碰 sibling。

### 6. 自己 last session 优先

先读自己的 journal → 展示"上次在这里做什么"。再读 sibling 作为补充。自己的 memory > sibling awareness。
