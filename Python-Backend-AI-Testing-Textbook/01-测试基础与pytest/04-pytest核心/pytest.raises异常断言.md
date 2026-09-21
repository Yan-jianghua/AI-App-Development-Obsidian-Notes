---
knowledge_id: py-ai-test-pytest-raises
title: pytest.raises 异常断言
project: Python 后端与 AI 应用测试教材
domain: pytest-core
note_type: concept
version: 1.0.0
status: current
created: 2026-09-18
updated: 2026-09-18
up: ["[[01-测试基础与pytest/00-学习导航]]"]
related:
  - "[[01-测试基础与pytest/02-测试术语/负向测试]]"
  - "[[01-测试基础与pytest/04-pytest核心/assert断言]]"
replaces: []
source_refs: [REF-FOUNDATIONS]
tags: [pytest/raises, testing/exceptions]
---

# pytest.raises 异常断言

## 作用

当需求规定非法输入必须抛出特定异常时，`pytest.raises` 验证异常确实发生且类型正确。

## 基本示例

```python
import pytest

def divide(a, b):
    if b == 0:
        raise ValueError("divisor must not be zero")
    return a / b

def test_divide_rejects_zero():
    with pytest.raises(ValueError):
        divide(10, 0)
```

如果没有异常，测试失败；如果抛出 TypeError，也失败，因为预期是 ValueError。

## 检查消息

```python
def test_divide_error_message():
    with pytest.raises(ValueError, match="must not be zero"):
        divide(10, 0)
```

`match` 是正则表达式。只检查稳定、属于契约的关键文本，不要绑定完整堆栈或会变化的内部措辞。

## 获取异常对象

```python
def test_error_contains_code():
    with pytest.raises(DomainError) as exc_info:
        perform_action()
    assert exc_info.value.code == "NOT_ALLOWED"
```

## 范围必须精确

```python
with pytest.raises(ValueError):
    prepare_data()
    divide(10, 0)
```

如果 `prepare_data()` 意外抛 ValueError，测试也会通过。应把 with 块限制到预期抛错的那一行。

## 常见错误

- 使用过宽的 `Exception`。
- 抛异常后还有断言写在 with 块内，那些代码不会执行。
- API 本应返回 400，却在 API 测试中期待 Python 异常。

## 练习与面试题

练习：测试提款金额为 0 和负数时抛出带错误码的异常。

面试：为什么 `pytest.raises(Exception)` 通常不是好测试？

