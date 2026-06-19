# Roadmap

## Phase 0: 当前（v2.4）→ 已完成

Context Engine v2.4。8 个子技能。反馈闭环。压缩。跨 agent 感知。git sync 层。

## Phase 1: 规范提取（v2.5）

**目标**：格式规范与实现分离。JSON 迁移。

**交付**：
1. `spec/context-spec-v1.md` — 正式格式规范（PROFILE/NARRATIVES/JOURNAL/GOALS/FEEDBACK/HANDOFF/PRIVACY）
2. 内存文件 Markdown → JSON 迁移
3. 隐私分层（public / agent:{id} / session）
4. Agent 交接信封格式

**工作量**：3-4 个会话

## Phase 2: Agent 深度互联（v2.6）

**目标**：交接协议实现。PROFILE 多源合并。

**交付**：
1. Handoff 协议实现
2. 交接消费确认 + 跨 agent 任务链追踪
3. PROFILE 合并算法

**工作量**：2-3 个会话

## Phase 3: 参考实现 & 社区（v3.0）

**目标**：Python 库 + LangChain 插件 + GitHub Release v1.0。

**工作量**：4-5 个会话

## Phase 4: 生态（v4.0）

**目标**：CrewAI / AutoGPT 插件 + VS Code 扩展。社区驱动。
