---
knowledge_id: py-ai-test-conftest
title: conftest.py 共享配置
project: Python 后端与 AI 应用测试教材
domain: pytest-core
note_type: concept
version: 1.0.0
status: current
created: 2026-09-18
updated: 2026-09-18
up: ["[[01-测试基础与pytest/00-学习导航]]"]
related: ["[[01-测试基础与pytest/04-pytest核心/pytest Fixture]]"]
replaces: []
source_refs: [REF-FOUNDATIONS]
tags: [pytest/conftest, testing/config]
---

# conftest.py 共享配置

## 它是什么

`conftest.py` 是 pytest 自动发现的本地插件文件，可以放共享 Fixture、Hook 和测试配置。测试文件通常不需要显式 import 其中的 Fixture。

## 目录示例

```text
tests/
├── conftest.py
├── unit/
│   └── test_price.py
└── api/
    └── test_users.py
```

`tests/conftest.py`：

```python
import pytest

@pytest.fixture
def sample_user():
    return {"id": 1, "name": "Alice"}
```

测试中直接请求：

```python
def test_user_name(sample_user):
    assert sample_user["name"] == "Alice"
```

## 作用范围

Fixture 对 `conftest.py` 所在目录及子目录可见。可以在子目录再放一个 `conftest.py`，提供更局部的资源或覆盖上层 Fixture。

## 应该放什么

真正被多个测试模块共享的基础设施、工厂和插件配置。只被一个文件使用的 Fixture 放在该测试文件更容易理解。

## 不要当普通工具模块

普通辅助函数最好放明确模块并显式 import。把所有内容塞进 conftest 会形成隐式依赖，难以搜索来源。

## 常见错误

- 在不同目录定义同名 Fixture，不知道实际用了哪个。
- conftest 导入应用时产生全局副作用。
- 文件过大，混合数据库、浏览器、AI 等所有资源。
- 测试试图 `import conftest`。

## 练习与面试题

练习：把两个测试文件重复的 `sample_user` 提取到 conftest，再用 `pytest --fixtures` 查看。

面试：为什么 Fixture 通常不需要从 conftest 显式导入？

