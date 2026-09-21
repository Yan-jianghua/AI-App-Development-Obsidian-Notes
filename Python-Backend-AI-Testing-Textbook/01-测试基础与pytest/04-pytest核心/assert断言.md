---
knowledge_id: py-ai-test-pytest-assert
title: assert 断言
project: Python 后端与 AI 应用测试教材
domain: pytest-core
note_type: concept
version: 1.0.0
status: current
created: 2026-09-18
updated: 2026-09-18
up: ["[[01-测试基础与pytest/00-学习导航]]"]
related:
  - "[[01-测试基础与pytest/02-测试术语/测试预言]]"
  - "[[01-测试基础与pytest/04-pytest核心/pytest.raises异常断言]]"
replaces: []
source_refs: [REF-FOUNDATIONS]
tags: [pytest/assert, testing/oracle]
---

# assert 断言

## 定义

断言表达“这个条件必须为真”。pytest 会改写普通 Python `assert`，失败时显示变量和值的差异。

## 常见写法

```python
assert result == 42
assert user.is_active
assert "token" in response
assert len(items) == 3
assert secret not in payload
```

## 失败示例

```python
def test_user_roles():
    actual = ["user", "editor"]
    assert actual == ["user", "admin"]
```

pytest 会显示列表在哪个位置不同，比手写 `if ...: print(...)` 更容易定位。

## 选择合适的比较

- 顺序重要：比较 list。
- 顺序不重要且无重复：比较 set。
- 需要保留重复但不关心顺序：使用 `collections.Counter`。
- 浮点数：使用 `pytest.approx`。
- 异常：使用 `pytest.raises`。

## 断言消息

```python
assert balance >= 0, f"余额不应为负，实际为 {balance}"
```

pytest 默认报告通常已足够。消息适合补充业务含义，不要重复“expected X got Y”。

## 一条测试能有多个断言吗

可以，只要共同验证同一个行为。例如创建用户后检查 ID、邮箱和密码未返回。若断言属于独立规则，拆成独立测试会使失败更清楚。

## 常见错误

- 使用 `assert function` 而不是 `assert function()`，函数对象本身总是真值。
- 用 `is` 比较字符串或数字；一般使用 `==`。
- 断言过于宽松，例如只检查结果非空。
- 断言整个不稳定响应，包含时间和随机 ID。

## 练习与面试题

练习：为返回用户字典的函数写 4 个有业务意义的断言。

面试：什么时候比较 list，什么时候比较 set？

