---
knowledge_id: py-ai-test-pytest-skip
title: pytest skip 跳过测试
project: Python 后端与 AI 应用测试教材
domain: pytest-core
note_type: concept
version: 1.0.0
status: current
created: 2026-09-18
updated: 2026-09-18
up: ["[[01-测试基础与pytest/00-学习导航]]"]
related:
  - "[[01-测试基础与pytest/04-pytest核心/pytest mark测试标记]]"
  - "[[01-测试基础与pytest/04-pytest核心/pytest xfail预期失败]]"
replaces: []
source_refs: [REF-FOUNDATIONS]
tags: [pytest/skip, testing/control]
---

# pytest skip 跳过测试

## 含义

Skip 表示当前条件下不执行测试。它不是通过，而是明确记录“没有运行”。

## 无条件跳过

```python
@pytest.mark.skip(reason="等待测试数据准备")
def test_import_legacy_file():
    ...
```

这种方式应短期使用，并记录负责人或任务。

## 条件跳过

```python
import sys
import pytest

@pytest.mark.skipif(
    sys.platform == "win32",
    reason="该功能只支持 Linux",
)
def test_linux_signal_handling():
    ...
```

只有 Windows 跳过，Linux 仍执行。

## 运行时跳过

```python
def test_gpu_feature():
    if not gpu_available():
        pytest.skip("当前环境没有 GPU")
    ...
```

## Skip 与删除

永久不再需要的测试应删除，而不是永远 skip。暂时环境不支持但未来需要，保留 skip 并监控数量。

## Skip 与 Xfail

Skip：测试不适用或无法运行；Xfail：测试应该运行，但已知当前会失败。两者表达完全不同的信息。

## 常见错误

- 为了让 CI 绿色而跳过失败测试。
- 没有 reason。
- 条件写反，关键平台全部跳过。
- 报表不显示跳过摘要，团队长期不知道覆盖缺口。

## 练习与面试题

练习：写一个只在 Python 3.12+ 运行的条件跳过示例。

面试：什么情况下应该 skip，什么情况下应该 xfail？

