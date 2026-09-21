---
knowledge_id: py-ai-test-pytest-parametrize
title: pytest.mark.parametrize 参数化
project: Python 后端与 AI 应用测试教材
domain: pytest-core
note_type: concept
version: 1.0.0
status: current
created: 2026-09-18
updated: 2026-09-18
up: ["[[01-测试基础与pytest/00-学习导航]]"]
related:
  - "[[01-测试基础与pytest/03-测试设计/边界值分析]]"
  - "[[01-测试基础与pytest/03-测试设计/决策表测试]]"
replaces: []
source_refs: [REF-FOUNDATIONS]
tags: [pytest/parametrize, testing/data-driven]
---

# pytest.mark.parametrize 参数化

## 作用

参数化让同一测试逻辑使用多组输入，每组会成为独立测试。它适合边界值、等价类和输入输出表。

## 示例

```python
import pytest

@pytest.mark.parametrize(
    "text,expected",
    [
        ("42", 42),
        (" 42 ", 42),
        ("+42", 42),
    ],
)
def test_parse_integer(text, expected):
    assert parse_integer(text) == expected
```

pytest 会运行三次。第二组失败时，报告会指出具体参数，不会阻止其他组执行。

## 使用 ids

```python
@pytest.mark.parametrize(
    "age,allowed",
    [(17, False), (18, True), (60, True), (61, False)],
    ids=["below-min", "min", "max", "above-max"],
)
def test_age(age, allowed):
    assert can_register(age) is allowed
```

清晰 ID 让报告更易读。

## 参数化异常

正常结果和异常结构差异较大时，可以拆成两个测试；不要为了“一个参数化解决所有”写复杂 if。

## 何时不使用

各场景准备、操作、断言完全不同；场景具有独立业务意义且需要明确名称；数据多到应成为独立数据文件或评测集。

## 常见错误

- 参数名称数量与数据列不一致。
- 把可变对象在多组间共享并修改。
- 在测试内部写循环，第一组失败后后续不执行。
- 参数矩阵过大造成组合爆炸。

## 练习与面试题

练习：参数化测试密码长度 7、8、64、65。

面试：参数化相比在测试中写 for 循环有什么优势？

