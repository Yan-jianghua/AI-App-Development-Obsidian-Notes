---
knowledge_id: py-ai-test-pytest-mark
title: pytest mark 测试标记
project: Python 后端与 AI 应用测试教材
domain: pytest-core
note_type: concept
version: 1.0.0
status: current
created: 2026-09-18
updated: 2026-09-18
up: ["[[01-测试基础与pytest/00-学习导航]]"]
related:
  - "[[01-测试基础与pytest/04-pytest核心/pytest skip跳过测试]]"
  - "[[01-测试基础与pytest/04-pytest核心/pytest xfail预期失败]]"
replaces: []
source_refs: [REF-FOUNDATIONS]
tags: [pytest/mark, testing/organization]
---

# pytest mark 测试标记

## 作用

Marker 给测试添加元数据，便于按类型、速度或依赖选择运行。常见自定义标记：`unit`、`integration`、`e2e`、`slow`、`gpu`。

## 示例

```python
import pytest

@pytest.mark.integration
def test_database_round_trip():
    ...
```

只运行集成测试：

```powershell
pytest -m integration
```

排除慢测试：

```powershell
pytest -m "not slow"
```

组合：

```powershell
pytest -m "integration and not slow"
```

## 注册标记

在 `pyproject.toml` 注册：

```toml
[tool.pytest.ini_options]
markers = [
  "unit: 快速且隔离的单元测试",
  "integration: 需要真实基础设施",
  "slow: 运行时间较长",
]
```

使用 `--strict-markers` 可让未注册或拼错的标记直接报错。

## 内置与自定义

`skip`、`skipif`、`xfail`、`parametrize` 也是 mark 机制。自定义标记只负责分类，不会自动改变测试行为，除非插件或 Hook 处理它。

## 常见错误

- `@pytest.mark.integartion` 拼错却未严格检查。
- 一条测试同时标 unit 和 integration，含义冲突。
- PR 只运行 unit，但从不在其他阶段运行被排除测试。
- 用 mark 替代合理目录结构。

## 练习与面试题

练习：注册 `unit` 和 `slow`，编写命令运行所有非 slow 用例。

面试：为什么自定义 Marker 应在配置中注册？

