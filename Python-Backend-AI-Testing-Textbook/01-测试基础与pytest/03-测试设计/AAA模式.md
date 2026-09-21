---
knowledge_id: py-ai-test-aaa-pattern
title: AAA 模式
project: Python 后端与 AI 应用测试教材
domain: test-structure
note_type: concept
version: 1.0.0
status: current
created: 2026-09-18
updated: 2026-09-18
up: ["[[01-测试基础与pytest/00-学习导航]]"]
related: ["[[01-测试基础与pytest/03-测试设计/Given-When-Then模式]]"]
replaces: []
source_refs: [CHAT-001, BASELINE-001]
tags: [testing/aaa, beginner]
---

# AAA 模式

## 定义

AAA 是 Arrange、Act、Assert：准备条件、执行行为、验证结果。它让测试像短故事一样容易阅读。

## 示例

```python
def test_withdraw_reduces_balance():
    # Arrange：准备账户和输入
    account = Account(balance=100)

    # Act：只执行主要行为
    account.withdraw(30)

    # Assert：检查可观察结果
    assert account.balance == 70
```

## Arrange

创建对象、数据和测试替身。只准备与本用例有关的内容；如果准备几十行，考虑 Factory 或 Fixture，但不要把关键条件隐藏掉。

## Act

通常只有一个主要动作。若执行多个业务操作，测试意图会变模糊；状态序列测试是合理例外。

## Assert

验证返回值、状态、异常和重要副作用。多个断言可以存在，只要共同证明同一行为。

## 为什么有用

当失败时能快速区分是准备失败、执行失败还是结果不对。评审者也能一眼看懂业务意图。

## 常见错误

- Act 后又继续 Arrange，结构混乱。
- 只有 Act，没有 Assert。
- Assert 内再次执行被测行为。
- 准备阶段调用太多业务流程，失败难定位。

## 练习与面试题

练习：把一个没有分段的注册测试改写为 AAA。

面试：一个测试可以有多个 Assert 吗？判断标准是什么？

