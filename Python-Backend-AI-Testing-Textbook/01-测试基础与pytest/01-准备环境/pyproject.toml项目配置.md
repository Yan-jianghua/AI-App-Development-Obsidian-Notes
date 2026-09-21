---
knowledge_id: py-ai-test-pyproject-toml
title: pyproject.toml 项目配置
project: Python 后端与 AI 应用测试教材
domain: python-environment
note_type: concept
version: 1.0.0
status: current
created: 2026-09-18
updated: 2026-09-18
up: ["[[01-测试基础与pytest/00-学习导航]]"]
related: ["[[01-测试基础与pytest/04-pytest核心/pytest命令行与失败排查]]"]
replaces: []
source_refs: [REF-FOUNDATIONS]
tags: [python/pyproject, testing/config]
---

# pyproject.toml 项目配置

## 一句话理解

`pyproject.toml` 是现代 Python 项目的统一配置文件，可描述项目、依赖和 pytest 等工具配置。

## 最小 pytest 配置

```toml
[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py"]
addopts = "-ra"
markers = [
  "unit: 快速单元测试",
  "integration: 需要真实依赖的集成测试",
]
```

逐项解释：

- `testpaths`：默认从 `tests` 目录寻找测试。
- `python_files`：测试文件命名规则。
- `addopts`：每次默认加入的命令参数；`-ra` 显示跳过、xfail 等摘要。
- `markers`：注册自定义标记，防止拼写错误。

## 为什么要把配置提交到 Git

团队成员和 CI 会使用同一套发现规则、标记和参数，避免“我这里能跑、你那里找不到测试”。

## 常见错误

- TOML 字符串、数组语法错误。
- 同时在 `pytest.ini`、`tox.ini` 和 `pyproject.toml` 定义冲突配置。
- 在 `addopts` 默认开启非常慢或只适合本机的参数。
- 随意忽略 warning，导致重要兼容问题被隐藏。

## 验证

运行：

```powershell
pytest --trace-config
```

它可以帮助确认 pytest 加载了哪些插件和配置。普通学习时运行 `pytest` 即可观察是否只搜索 `tests`。

## 练习与面试题

练习：注册 `slow` 标记，并用命令只运行非 slow 测试。

面试：把 pytest 配置放进项目文件有什么团队价值？

