---
knowledge_id: py-ai-test-pytest-approx
title: pytest.approx 浮点近似
project: Python 后端与 AI 应用测试教材
domain: pytest-core
note_type: concept
version: 1.0.0
status: current
created: 2026-09-18
updated: 2026-09-18
up: ["[[01-测试基础与pytest/00-学习导航]]"]
related: ["[[01-测试基础与pytest/04-pytest核心/assert断言]]"]
replaces: []
source_refs: [REF-FOUNDATIONS]
tags: [pytest/approx, testing/floating-point]
---

# pytest.approx 浮点近似

## 为什么需要

二进制浮点数不能精确表示很多十进制小数：

```python
>>> 0.1 + 0.2
0.30000000000000004
```

因此直接 `== 0.3` 可能失败，即使数学意义上结果正确。

## 基本用法

```python
import pytest

def test_add_decimal_floats():
    assert 0.1 + 0.2 == pytest.approx(0.3)
```

`approx` 允许一个很小的相对或绝对误差。

## 指定容差

```python
assert measured == pytest.approx(100.0, rel=0.01)
assert measured == pytest.approx(100.0, abs=0.5)
```

- `rel=0.01`：允许约 1% 相对误差。
- `abs=0.5`：允许绝对相差 0.5。

容差应来自业务或数值算法要求，不能为了让测试通过随意放大。

## 列表和字典

```python
assert [0.1 + 0.2, 1.0] == pytest.approx([0.3, 1.0])
```

## 金额注意

财务金额通常使用 `Decimal` 和明确舍入规则，不应依靠模糊容差。`approx` 更适合科学计算、测量和浮点模型结果。

## 常见错误

- 对整数或精确字符串使用 approx。
- 容差大到掩盖真实 Bug。
- 财务金额用 float，测试只能近似。

## 练习与面试题

练习：为摄氏转华氏函数写带合理容差的测试。

面试：为什么 `0.1 + 0.2 == 0.3` 可能为 False？财务金额应如何处理？

