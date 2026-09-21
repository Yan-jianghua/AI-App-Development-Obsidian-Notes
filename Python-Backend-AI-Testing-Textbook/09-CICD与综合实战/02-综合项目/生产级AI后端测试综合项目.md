---
knowledge_id: py-ai-textbook-part09-1772bb6771f0
title: "生产级 AI 后端测试综合项目"
project: Python 后端与 AI 应用测试教材
domain: capstone
note_type: project
version: 1.0.0
status: current
created: 2026-09-18
updated: 2026-09-18
up: ["[[09-CICD与综合实战/00-学习导航]]"]
related: []
replaces: []
source_refs: [CHAT-001]
tags: [course/capstone]
---


# 生产级 AI 后端测试综合项目

## 项目目标

构建并测试一个“企业知识库问答 API”：用户登录后上传文档，系统异步解析和建立向量索引，通过 RAG 回答并给出引用；管理员可查看评测与运行指标。

## 最小架构

```text
客户端 → FastAPI → PostgreSQL
                → Redis / 后台任务
                → 对象存储
                → 向量数据库 → LLM
                → 日志、指标、追踪
```

## 阶段一：可测试的业务骨架

- 用 Pydantic 定义请求和响应。
- Repository 隔离持久化。
- 外部 LLM、Embedding、对象存储通过依赖注入传入。
- 用 pytest 覆盖权限、输入校验和核心业务规则。

验收：无网络时单元测试可运行；错误信息清楚；测试无顺序依赖。

## 阶段二：真实集成

- 使用 Testcontainers 启动 PostgreSQL 与 Redis。
- 测试迁移从空库升级到 head。
- 测试事务回滚、唯一约束、缓存失效和后台任务重试。
- 对象存储使用 MinIO 或隔离测试 bucket。

验收：重复运行三次结果一致，所有临时资源可清理。

## 阶段三：RAG 评测

- 建立至少 100 条带参考答案和证据的评测集。
- 分别计算 Recall@K、MRR、上下文精确率、忠实性与引用准确性。
- 比较两种 chunk size、两种检索器和是否启用 reranker。
- 保存模型、Embedding、索引、Prompt 与数据集版本。

验收：能定位一个失败究竟发生在解析、检索、重排还是生成。

## 阶段四：安全与可靠性

- 覆盖对象级授权、路径遍历、SSRF、Prompt Injection 与知识库投毒。
- 对所有副作用工具加入参数校验、最小权限和人工确认。
- 进行负载、峰值和故障注入测试。
- 验证日志脱敏、Trace 贯通、告警与运行手册。

验收：攻击样本不能跨租户取数；下游超时不会无限重试；关键告警可触发。

## 阶段五：CI/CD

拉取请求门禁：Ruff、类型检查、单元测试、关键集成测试、SAST、依赖审计。夜间任务：全量 E2E、RAG 评测、变异测试和负载基线。发布使用不可变镜像、灰度、指标护栏和自动回滚。

## 最终交付清单

- 测试策略与风险矩阵。
- 可重复测试环境与锁文件。
- 单元、集成、契约、E2E、安全、性能和 AI 评测报告。
- 失败样本与回归数据集。
- CI 配置、质量门禁、发布与回滚说明。
- 运行手册、告警说明和灾难恢复演练记录。
