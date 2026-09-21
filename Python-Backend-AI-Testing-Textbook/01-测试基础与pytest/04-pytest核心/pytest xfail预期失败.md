---
knowledge_id: py-ai-test-pytest-xfail
title: pytest xfail 预期失败
project: Python 后端与 AI 应用测试教材
domain: pytest-core
note_type: concept
version: 1.0.0
status: current
created: 2026-09-18
updated: 2026-09-18
up: ["[[01-测试基础与pytest/00-学习导航]]"]
related: ["[[01-测试基础与pytest/04-pytest核心/pytest skip跳过测试]]"]
replaces: []
source_refs: [REF-FOUNDATIONS]
tags: [pytest/xfail, testing/control]
---

# pytest xfail 预期失败

## 含义

Xfail 表示测试代表正确需求，但当前实现有已知缺陷，预计会失败。pytest 仍执行它，并把失败报告为 XFAIL。

## 示例

```python
@pytest.mark.xfail(
    reason="BUG-123：闰年日期解析尚未修复",
    strict=True,
)
def test_parse_february_29():
    assert parse_date("2024-02-29").day == 29
```

## XPASS

如果测试意外通过，称为 XPASS。`strict=True` 会把 XPASS 当失败，提醒团队移除 xfail 并确认 Bug 已真正修复。

## 限定异常

```python
@pytest.mark.xfail(raises=KnownParserError, reason="已知解析缺陷")
def test_case():
    ...
```

如果出现其他异常，不应被当作预期失败掩盖。

## 使用原则

Xfail 是短期风险登记，不是永久垃圾桶。应关联 Issue、负责人和复查时间。严重安全或数据破坏测试不应仅 xfail 后继续发布。

## 与 Skip 区别

Xfail 会执行，说明当前实现不符合需求；Skip 不执行，说明场景不适用或环境不足。

## 常见错误

- 不设置 strict，Bug 修复后 XPASS 被忽略。
- 预期任意失败，掩盖新异常。
- 用 xfail 处理 Flaky Test。
- 没有 Issue 和清理计划。

## 练习与面试题

练习：为一个已知 Bug 写 strict xfail，并模拟修复后观察 XPASS。

面试：为什么 `strict=True` 对长期维护有价值？

