---
knowledge_id: py-ai-test-pytest-fixture-scope
title: Fixture 作用域
project: Python 后端与 AI 应用测试教材
domain: pytest-core
note_type: concept
version: 1.0.0
status: current
created: 2026-09-18
updated: 2026-09-18
up: ["[[01-测试基础与pytest/00-学习导航]]"]
related:
  - "[[01-测试基础与pytest/04-pytest核心/pytest Fixture]]"
  - "[[01-测试基础与pytest/04-pytest核心/yield Fixture与资源清理]]"
replaces: []
source_refs: [REF-FOUNDATIONS]
tags: [pytest/fixture-scope, testing/isolation]
---

# Fixture 作用域

## 作用域控制什么

Fixture 作用域决定资源创建一次后可以被多少测试复用，以及何时清理。

| scope | 创建频率 | 适合 |
|---|---|---|
| function | 每个测试一次 | 可变业务数据、默认选择 |
| class | 每个测试类一次 | 类内共享只读资源 |
| module | 每个测试文件一次 | 较昂贵且稳定的资源 |
| package | 每个测试包一次 | 大型模块级基础设施 |
| session | 整次 pytest 一次 | 数据库容器、只读模型 |

## 示例

```python
@pytest.fixture(scope="session")
def database_container():
    container = start_postgres()
    yield container
    container.stop()

@pytest.fixture(scope="function")
def db_session(database_container):
    session = open_session(database_container)
    yield session
    session.rollback()
    session.close()
```

容器启动昂贵，所以 session 级；业务事务必须隔离，所以 function 级。

## 缓存行为

同一作用域内多次请求同一个 Fixture，pytest 复用结果。若结果是可变列表，一个测试修改后可能影响同作用域其他测试。

## 选择原则

默认 function 最安全。只有测量表明创建资源很昂贵，并且能够确保状态隔离时，才扩大作用域。扩大作用域是性能优化，也增加污染风险。

## 依赖约束

大作用域 Fixture 不能依赖更小作用域 Fixture，因为其生命周期不匹配。设计时让基础设施在外层，测试数据在内层。

## 常见错误

- session 级共享可变用户或数据库会话。
- 为加速盲目扩大作用域，导致顺序依赖。
- 清理范围与创建范围不一致。

## 练习与面试题

练习：为 Docker 数据库、数据库连接、事务、测试用户分别选择 scope 并说明理由。

面试：为什么 session 级 Fixture 更快却更危险？

