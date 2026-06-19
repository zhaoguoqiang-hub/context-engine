# AContext — Open Standard for Agent Context

## 愿景

AI agent 记忆的可移植文件系统。

就像 `.git` 让版本控制跨编辑器可移植，AContext 让 agent 的身份、
记忆和关系数据跨平台、跨模型、跨 agent 可移植。

用户在哪个 agent 上工作，就把自己的 context 带到哪。
不是"在 ChatGPT 里训练一个助手"，而是"我拥有我的 AI 关系数据"。

## 为什么叫 AContext

Agent Context。短。文件级。不是"灵魂"——太玄。不是"记忆层"——太工程。
AContext = 每个 agent 都能理解的上下文文件。

## 成熟形态（Phase 5 完成时）

~/.acontext/                  ← 一个目录。放下就能用。
├── spec.md                   ← 格式规范（任何 agent 可实现）
├── profile.json              ← 用户身份（标准 schema）
├── goals.json                ← 活跃目标
├── adaptations.json          ← 习得的行为规则
├── narratives.jsonl          ← 跨 agent 共享叙事时间线
├── reflections.json          ← 长期洞察
├── feedback.jsonl            ← 反馈学习信号
├── journals/
│   ├── {agent_id}.jsonl      ← 按 agent 分账本，零冲突
├── handoffs/
│   ├── {agent_id}.json       ← Agent 间结构化交接信封
├── privacy.json              ← 隐私分层：跨 agent / 单 agent / 临时
├── archive/                  ← 压缩后的旧数据
└── devices/                  ← 多设备同步追踪

实现层：
├── skills/context-engine/    ← SKILL.md 参考实现（Hermes/Codex）
├── libs/
│   ├── python/acontext/      ← Python 库：读/写/校验 spec
│   └── node/acontext/        ← Node.js 库
└── plugins/
    ├── langchain/            ← LangChain 记忆后端
    └── crewai/               ← CrewAI 记忆后端

## 设计原则

1. **文件即 API** — 不需要服务器，不需要数据库。JSON 文件就是数据层。
2. **规范优先实现** — spec.md 定义兼容性。实现可以有多个。
3. **可携带** — 一个目录 `cp -r` 就能迁移。
4. **可检验** — 用户随时 `cat` 看懂自己的数据。
5. **默认最小** — 不需要的内存不创建。不需要的字段不写入。
6. **隐私内置** — 每个条目标注可见范围。用户完全控制删除。
