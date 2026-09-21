---
knowledge_id: py-ai-test-given-when-then
title: Given-When-Then 模式
project: Python 后端与 AI 应用测试教材
domain: test-structure
note_type: concept
version: 1.0.0
status: current
created: 2026-09-18
updated: 2026-09-18
up: ["[[01-测试基础与pytest/00-学习导航]]"]
related:
  - "[[01-测试基础与pytest/03-测试设计/AAA模式]]"
  - "[[01-测试基础与pytest/02-测试术语/验收测试]]"
replaces: []
source_refs: [CHAT-001, BASELINE-001]
tags: [testing/bdd, beginner]
---

# Given-When-Then 模式

## 定义

Given-When-Then 用业务语言描述场景：给定什么背景，当发生什么行为，那么应该看到什么结果。它与 AAA 基本对应，但更强调业务可读性。

## 示例

```text
Given 账户余额为 100 元
When 用户取款 30 元
Then 账户余额应为 70 元
```

对应 pytest：

```python
def test_withdraw_reduces_balance():
    # Given
    account = Account(balance=100)
    # When
    account.withdraw(30)
    # Then
    assert account.balance == 70
```

## And 与 But

可以增加相关条件，例如 `And 账户未冻结`，但不要让场景无限增长。多个独立行为应拆分。

## 与 BDD

BDD 强调开发、测试和业务共同通过示例澄清行为。Gherkin/Cucumber 只是工具形式；即使不用专门框架，也可以用 Given-When-Then 改善沟通。

## 适用场景

验收标准、状态转换、权限和跨角色业务流程。对底层数学函数，直接 AAA 往往更简洁。

## 常见错误

- 把 UI 点击细节写进业务场景。
- Then 使用“系统正常”“体验良好”等不可验证词。
- 场景文件与自动化实现脱节。

## 练习与面试题

练习：为“过期优惠券不能使用”写一个 Given-When-Then 场景。

面试：Given-When-Then 与 AAA 的主要差异是什么？

