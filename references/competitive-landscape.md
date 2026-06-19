# 竞争格局分析

## 同类产品

### Mem0
- **定位**：开发者用的 AI memory API
- **模式**：云端托管或自部署。需要 API key。SDK（Python/JS）
- **开源**：是（mem0ai/mem0，~20K+ stars）
- **用户**：开发者构建 AI app 时调用它做记忆层
- **与 AContext 差异**：API 中心，不是文件标准。需要一个运行的服务器。不解决"用户自己带着记忆跨 agent"

### Letta（原 MemGPT）
- **定位**：有状态 LLM 框架
- **模式**：自部署服务器。虚拟上下文管理 + 记忆层级（core/archival）
- **开源**：是（letta-ai/letta，~13K+ stars）
- **用户**：想给单个 AI 应用加记忆的开发者
- **与 AContext 差异**：服务器 + 框架。不是文件标准。为单一应用设计，不跨平台

### Zep
- **定位**：企业级 AI assistant 记忆层
- **模式**：云端 SaaS。企业付费。
- **开源**：部分（~2K+ stars）
- **用户**：企业 AI 客服/助手
- **与 AContext 差异**：商业产品，不是标准。数据在云端，不在用户手里

### LangChain Memory
- **定位**：框架内置记忆模块
- **模式**：代码级。buffer/summary/vector 多种后端
- **用户**：所有 LangChain 用户（默认可用）
- **与 AContext 差异**：框架级，不跨平台。在进程里，不是文件。每个 app 独立实现，记忆不随用户走

### Cursor Rules (.cursorrules)
- **定位**：编辑器级规则文件
- **模式**：项目目录下 `.cursorrules` 文件
- **用户**：Cursor 用户
- **与 AContext 差异**：局限在单个编辑器。只是规则指令，不是用户记忆/画像

### CLAUDE.md / AGENTS.md
- **定位**：Agent 指令文件
- **模式**：项目或用户目录下的 markdown
- **用户**：Claude Code / Codex 用户
- **与 AContext 差异**：是指令不是记忆。不存用户画像、叙事、反馈。但格式方向是对的——文件级、可移植

## 当前格局总结

```
            云端/API ←──────────────→ 文件/本地
              │                        │
    Mem0      │                        │  AContext ★
    Letta     │    Cursor Rules        │
    Zep       │    CLAUDE.md           │
    LangChain │    AGENTS.md           │
              │                        │
            平台/框架 ←─────────────→ 标准/可移植
```

**AContext 是唯一处于"文件/本地 + 标准/可移植"象限的产品。**

## 真实风险

1. **Mem0 或 Letta 加入文件模式**：如果它们支持本地 JSON 文件导出，会成为直接竞争者。但它们的架构是 API 中心的，加入文件模式是附加功能，不是核心设计。

2. **OpenAI 开放记忆导出**：如果 ChatGPT 允许导出记忆为 JSON，会有大量用户提取数据。但 OpenAI 没有动机做这件事——锁定是他们的利益。

3. **Apple Intelligence 的本地 agent 层**：如果 Apple 在 macOS 上做本地 agent 上下文层，它会成为默认选择（对所有 Mac 用户）。但这会是 Apple 专属的，不跨平台。

4. **没有人做这个是因为市场不存在**：最诚实的风险。也许"用户带着自己的 AI 记忆跨平台"不是一个真实需求。但以下信号表明是：
   - 多 agent 使用在增长（Codex + Hermes + Cursor + Claude）
   - AI 用户抱怨"每次都要重新解释"
   - Cursor Rules 和 CLAUDE.md 的出现说明用户确实想要文件级的 agent 配置。但只是指令，不是记忆。
