---
knowledge_id: py-ai-test-pytest-discovery
title: pytest 测试发现
project: Python 后端与 AI 应用测试教材
domain: pytest-core
note_type: concept
version: 1.0.0
status: current
created: 2026-09-18
updated: 2026-09-18
up: ["[[01-测试基础与pytest/00-学习导航]]"]
related:
  - "[[01-测试基础与pytest/04-pytest核心/pytest测试框架]]"
  - "[[01-测试基础与pytest/01-准备环境/pyproject.toml项目配置]]"
replaces: []
source_refs: [REF-FOUNDATIONS]
tags: [pytest/discovery, testing/python]
---

# pytest 测试发现

## 什么是测试发现

测试发现（Collection）是 pytest 在执行前寻找“哪些文件、类和函数属于测试”的过程。

## 常见默认规则

- 文件名：`test_*.py` 或 `*_test.py`。
- 函数和方法：以 `test_` 开头。
- 测试类：常以 `Test` 开头，并且通常不要自定义 `__init__`。

```python
def test_login_success():  # 会被发现
    assert True

def login_test():          # 默认不会被发现
    assert True
```

## 查看收集结果

```powershell
pytest --collect-only -q
```

这个命令不运行测试，只显示找到的节点。遇到“明明写了测试却没执行”时首先使用。

## Node ID

pytest 用节点 ID 唯一表示测试，例如：

```text
tests/test_login.py::TestLogin::test_success
```

可以只运行它：

```powershell
pytest tests/test_login.py::TestLogin::test_success
```

## 配置规则

可以在 `pyproject.toml` 修改 `testpaths`、`python_files`、`python_classes`、`python_functions`，但团队应保持简单一致。

## 导入问题

pytest 收集时会导入测试模块。如果模块路径、包结构或循环导入错误，测试还没执行就会 collection error。应从项目根目录运行并采用一致的打包方式。

## 常见错误

- 测试函数嵌套在普通函数中。
- 文件名是 `tests.py` 但配置只接受 `test_*.py`。
- 同名测试函数后一个覆盖前一个。
- 测试类定义 `__init__`，无法正常收集。

## 练习与面试题

练习：创建一个符合规则和一个不符合规则的测试，用 `--collect-only` 观察。

面试：pytest 的 collection error 与 test failure 有何区别？

