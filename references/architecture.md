# 原版架构设计（Plugin 版，仅供参考）

此文件保留原始 Plugin 层设计方案，供理解完整设计意图。
当前 v2.0 纯 Skill 版已用 SKILL.md 指令替代所有 Plugin 代码。

## 原 Plugin: proactive-engine

- GoalManager: 硬编码 3 个核心目标，子目标动态派生
- ReflectionThread: 后台反思，空闲期自动启动
- RuntimeStore: 持久化状态（goals/daily_context/mood/narratives/signals）
- ProactiveAPI: 对外 tool 接口（soul_* 工具链）

## 原定时任务（Plugin 版用 cron 实现）

| 任务 | 频率 | 用途 |
|------|------|------|
| value-guard-boundary | 每30分钟 | 边界检查 |
| signal-distributor | 每15分钟 | 信号分发 |
| proactive-check | 每2小时 | 主动建议检查 |
| narrative-daily | 每天2点 | 每日叙事分析 |
| value-guard-full | 每天3点 | 全面价值评估 |
| system-watchdog | 每小时 | 健康检查+补偿 |

## 迁移说明

v2.0 纯 Skill 版中，所有定时任务转化为会话生命周期钩子：

| 原定时任务 | v2.0 替代方案 |
|-----------|--------------|
| 每30分钟边界检查 | 会话开始 + 每次回复前检查 |
| 每15分钟信号分发 | 检测到信号事件时立即分发 |
| 每2小时主动检查 | 会话开始 + 每5轮对话后 |
| 每天2点叙事分析 | 会话开始检测距上次整合 > 24h |
| 每天3点全面评估 | 会话结束反思阶段 |
| 每小时健康检查 | 会话开始读取状态文件 |

## 控制面板（已移除）

原设计包含 midnight-galaxy 主题 Web UI，v2.0 中移除。
所有状态通过 memory/ 文件直接查看，无需额外 UI。

