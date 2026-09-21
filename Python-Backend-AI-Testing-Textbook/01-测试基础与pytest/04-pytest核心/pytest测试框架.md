---
knowledge_id: py-ai-test-pytest-framework
title: pytest 测试框架
project: Python 后端与 AI 应用测试教材
domain: pytest-core
note_type: concept
version: 1.0.0
status: current
created: 2026-09-18
updated: 2026-09-18
up: ["[[01-测试基础与pytest/00-学习导航]]"]
related:
  - "[[01-测试基础与pytest/01-准备环境/pip包管理器]]"
  - "[[01-测试基础与pytest/04-pytest核心/pytest测试发现]]"
replaces: []
source_refs: [REF-FOUNDATIONS]
tags: [package/pytest, testing/python]
---

# pytest 测试框架

## 它是什么

pytest 是 Python 常用测试框架。它负责发现测试、运行测试、显示断言差异，并提供 Fixture、参数化、标记和插件机制。

## 安装

激活虚拟环境后：

```powershell
python -m pip install pytest
pytest --version
```

## 第一个项目

```text
project/
├── calculator.py
└── tests/
    └── test_calculator.py
```

`calculator.py`：

```python
def add(a: int, b: int) -> int:
    return a + b
```

`tests/test_calculator.py`：

```python
from calculator import add

def test_add_two_numbers():
    assert add(2, 3) == 5
```

在项目根目录执行：

```powershell
pytest
```

pytest 找到 `test_` 文件和函数，执行 `add(2, 3)`，然后用 assert 比较 5。正确时显示 passed；若函数错误返回 6，pytest 会显示实际值和期望值差异。

## pytest 的优点

- 使用普通 `assert`，语法简洁。
- Fixture 组合灵活。
- 参数化减少重复。
- 插件生态覆盖异步、覆盖率、浏览器和并行。
- 可以运行 unittest 风格测试，便于迁移。

## 测试不是脚本

不要在文件末尾手工调用 `test_add_two_numbers()`。pytest 负责收集、隔离、报告和退出码；CI 根据退出码判断成功或失败。

## 常见错误

- 文件或函数没按规则命名，显示 collected 0 items。
- 在错误目录运行，模块导入失败。
- pytest 安装在另一个 Python 环境。
- 测试中用 print 判断结果，没有 assert。

## 练习与面试题

练习：创建 `subtract` 函数和两条测试，故意让一条失败并阅读报告。

面试：pytest 相比手工运行测试函数提供了哪些能力？

## 官方资料

https://docs.pytest.org/en/stable/

