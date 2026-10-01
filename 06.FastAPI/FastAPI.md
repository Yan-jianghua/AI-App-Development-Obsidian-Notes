# FastAPI 学习导航

## 独立关键词笔记

- [[06.FastAPI/1.入门与项目结构/001.ASGI与生命周期|ASGI与生命周期]]
- [[06.FastAPI/2.Pydantic与数据校验/001.输入输出Schema|输入输出Schema]]
- [[06.FastAPI/3.路由与依赖注入/001.依赖注入|依赖注入]]
- [[06.FastAPI/4.数据库与事务/001.请求事务边界|请求事务边界]]
- [[06.FastAPI/5.认证授权与安全/001.认证与对象级授权|认证与对象级授权]]
- [[06.FastAPI/6.异步 流式与后台任务/001.async与阻塞调用|async与阻塞调用]]
- [[06.FastAPI/6.异步 流式与后台任务/002.SSE与取消传播|SSE与取消传播]]
- [[06.FastAPI/7.测试 部署与可观测性/001.API契约与可观测性|API契约与可观测性]]

FastAPI 用 Python 类型提示描述 API 输入输出，结合 Pydantic 校验数据，并运行在 ASGI 生态上。学习重点是 API 边界、依赖管理与异步资源，而不只是会写装饰器。

## 推荐顺序

1. [[00.入门与项目结构]]
2. [[00.Pydantic与数据校验]]
3. [[00.路由与依赖注入]]
4. [[00.数据库与事务]]
5. [[00.认证授权与安全]]
6. [[00.异步 流式与后台任务]]
7. [[00.测试 部署与可观测性]]

## 最小应用

```python
from fastapi import FastAPI

app = FastAPI(title="Notes API")

@app.get("/health")
async def health() -> dict[str, bool]:
    return {"ok": True}
```

开发阶段运行：`uvicorn app.main:app --reload`。`--reload` 仅用于开发；生产环境要考虑进程数、反向代理、超时、健康检查和优雅停机。

## 学完应能做到

- 设计 REST 风格端点和一致错误响应。
- 使用 Pydantic 做输入、输出和配置校验。
- 用依赖注入管理认证、数据库会话和可替换服务。
- 正确选择 `def`/`async def`，避免阻塞事件循环。
- 编写自动化测试并安全部署。

官方资料：[FastAPI Documentation](https://fastapi.tiangolo.com/)、[Pydantic Documentation](https://docs.pydantic.dev/)。

## 综合练习与验收

扩展最小应用为待办 API：创建、读取、更新和删除任务，定义分离的输入/输出模型，使用依赖注入取得用户与数据库会话。为跨用户读取、字段缺失、重复创建、乐观锁冲突和数据库异常分别写测试。验收时应能证明事务异常后回滚、会话被关闭、响应不泄漏内部字段；再模拟客户端中断流式请求，确认上游任务和连接得到释放。
