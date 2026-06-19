# 多 Agent 共享灵魂系统

## 问题

用户同时使用多个 agent（Codex、Hermes），每个 agent 有独立的沙箱和会话。
灵魂系统需要：同一个用户画像、同一段叙事记忆、互相知道对方做了什么。

## 方案：单一数据层 + 按 agent 分账本

```
~/.agents/skills/soul-system/memory/   ← 数据层（唯一）
├── PROFILE.md          ← 共享（所有 agent 读同一份）
├── GOALS.md            ← 共享
├── ADAPTATIONS.md      ← 共享
├── REFLECTIONS.md      ← 共享
├── NARRATIVES.md       ← 共享，append-only，条目标记 agent 来源
├── journals/
│   ├── codex.md        ← Codex 专属（不冲突）
│   └── hermes.md       ← Hermes 专属（不冲突）
└── META.md             ← agent 注册表
```

~/.codex/skills/soul-system → symlink → ~/.agents/skills/soul-system

## 为什么不会冲突

| 文件 | 写入模式 | 冲突概率 |
|------|---------|---------|
| journals/*.md | 各自写各自的 | 零 |
| NARRATIVES.md | append-only + `[agent:xxx]` 标签 | 零（追加不覆盖） |
| PROFILE.md | 时间戳 last-write-wins | 极低（几乎不同时写） |
| GOALS.md | 手动修改 | 零 |
| ADAPTATIONS.md | 追加规则 | 极低 |

## 跨 Agent 感知

每个 agent 启动时读取：

1. 自己的 journal → 知道自己上次做了什么
2. 兄弟 journal → 知道其他 agent 最近做了什么
3. 共享 NARRATIVES → 知道用户最近的里程碑/决策

效果：Codex 能说 "Hermes 刚帮你部署了那个服务，现在有什么要接手的？"

## 首次安装（Codex 侧）

```bash
ln -sfn ~/.agents/skills/soul-system ~/.codex/skills/soul-system
```

## Agent 注册

编辑 `memory/META.md`，添加 agent 后必须注册：

```yaml
agents:
  hermes:
    id: hermes
    role: 任务自动化 + 三省六部
    active: true
  codex:
    id: codex
    role: 开发 + 深度分析
    active: true
```
