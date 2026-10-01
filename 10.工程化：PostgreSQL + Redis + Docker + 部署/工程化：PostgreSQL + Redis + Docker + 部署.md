# 工程化学习导航：PostgreSQL + Redis + Docker + 部署

## 独立关键词笔记

- [[10.工程化：PostgreSQL + Redis + Docker + 部署/1.PostgreSQL数据建模与事务/001.主键外键与唯一约束|主键外键与唯一约束]]
- [[10.工程化：PostgreSQL + Redis + Docker + 部署/1.PostgreSQL数据建模与事务/002.隔离级别与并发控制|隔离级别与并发控制]]
- [[10.工程化：PostgreSQL + Redis + Docker + 部署/2.SQLAlchemy与迁移/001.Session生命周期|Session生命周期]]
- [[10.工程化：PostgreSQL + Redis + Docker + 部署/2.SQLAlchemy与迁移/002.数据库迁移|数据库迁移]]
- [[10.工程化：PostgreSQL + Redis + Docker + 部署/3.Redis缓存与任务/001.缓存键与失效|缓存键与失效]]
- [[10.工程化：PostgreSQL + Redis + Docker + 部署/3.Redis缓存与任务/002.队列幂等与重试|队列幂等与重试]]
- [[10.工程化：PostgreSQL + Redis + Docker + 部署/4.Docker与Compose/001.Docker镜像与最小权限|Docker镜像与最小权限]]
- [[10.工程化：PostgreSQL + Redis + Docker + 部署/5.CI CD与部署/001.CI质量门禁|CI质量门禁]]
- [[10.工程化：PostgreSQL + Redis + Docker + 部署/5.CI CD与部署/002.灰度发布与回滚|灰度发布与回滚]]
- [[10.工程化：PostgreSQL + Redis + Docker + 部署/6.可观测性 安全与恢复/001.日志指标与追踪|日志指标与追踪]]
- [[10.工程化：PostgreSQL + Redis + Docker + 部署/6.可观测性 安全与恢复/002.备份恢复与灾难演练|备份恢复与灾难演练]]

应用写出来只是开始。上线还需要可靠的数据存储、缓存、容器化、配置、迁移、监控、备份和恢复。建议在完成 FastAPI 基础后学习本章。

## 推荐顺序

1. [[00.PostgreSQL数据建模与事务]]
2. [[00.SQLAlchemy与迁移]]
3. [[00.Redis缓存与任务]]
4. [[00.Docker与Compose]]
5. [[00.CI CD与部署]]
6. [[00.可观测性 安全与恢复]]

## 上线闭环

```text
代码/依赖锁定 → 自动测试 → 构建镜像 → 数据库迁移
→ 灰度/滚动发布 → 健康检查 → 监控 → 备份与回滚演练
```

所有示例均需按实际环境补齐凭证、地址和版本。不要把开发环境中的默认密码带到公网部署。

## 综合练习与验收

将 FastAPI 服务、PostgreSQL、Redis 组成可重复启动的开发环境。增加唯一约束、数据库迁移、缓存失效、Outbox 事件与幂等消费者；在 CI 中执行静态检查、单元和集成测试。发布时先演练旧新版本同时运行，再做灰度切流与回滚。验收报告记录连接池耗尽、Redis 不可用、迁移失败、备份恢复四种故障的实际错误率、P95 延迟、RPO 和 RTO；任何数字都应来自测试记录。
