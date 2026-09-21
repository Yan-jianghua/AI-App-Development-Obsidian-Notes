---
knowledge_id: py-ai-test-pytest-fixture
title: pytest Fixture
project: Python 后端与 AI 应用测试教材
domain: pytest-core
note_type: concept
version: 1.0.0
status: current
created: 2026-09-18
updated: 2026-09-18
up: ["[[01-测试基础与pytest/00-学习导航]]"]
related:
  - "[[01-测试基础与pytest/04-pytest核心/Fixture作用域]]"
  - "[[01-测试基础与pytest/04-pytest核心/yield Fixture与资源清理]]"
replaces: []
source_refs: [REF-FOUNDATIONS]
tags: [pytest/fixture, testing/setup]
---

# pytest Fixture

## 白话解释

Fixture 是 pytest 管理测试前置资源的方法。测试函数通过参数名声明“我需要这个资源”，pytest 负责创建并传入。

## 基本示例

```python
import pytest

@pytest.fixture
def user():
    return {"name": "Alice", "role": "admin"}

def test_admin_user_has_role(user):
    assert user["role"] == "admin"
```

pytest 看到参数 `user`，找到同名 Fixture，先执行它，再把返回值传给测试。

## Fixture 依赖

```python
@pytest.fixture
def repository():
    return InMemoryUserRepository()

@pytest.fixture
def saved_user(repository):
    return repository.create("alice@example.com")

def test_user_is_saved(repository, saved_user):
    assert repository.get(saved_user.id) is not None
```

pytest 会按依赖顺序准备。

## Fixture 与普通辅助函数

普通函数由测试主动调用；Fixture 由 pytest 注入，并能管理作用域、清理和依赖。简单纯数据不一定都要 Fixture，避免隐藏关键输入。

## Factory Fixture

当测试需要多个不同用户时，返回创建函数比固定用户更灵活：

```python
@pytest.fixture
def make_user():
    def factory(role="user"):
        return User(role=role)
    return factory
```

## 常见错误

- 直接调用 Fixture 函数，而不是通过参数请求。
- Fixture 做大量业务操作，测试正文看不出前置条件。
- 所有数据都变成全局 Fixture，难以理解和维护。
- 返回可变对象并在大作用域中共享。

## 练习与面试题

练习：写 `make_order` Factory Fixture，可传入金额和状态。

面试：Fixture 和普通辅助函数的主要区别是什么？

