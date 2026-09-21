---
knowledge_id: py-ai-test-pip
title: pip 包管理器
project: Python 后端与 AI 应用测试教材
domain: python-environment
note_type: concept
version: 1.0.0
status: current
created: 2026-09-18
updated: 2026-09-18
up: ["[[01-测试基础与pytest/00-学习导航]]"]
related:
  - "[[01-测试基础与pytest/01-准备环境/venv虚拟环境]]"
  - "[[01-测试基础与pytest/04-pytest核心/pytest测试框架]]"
replaces: []
source_refs: [REF-FOUNDATIONS]
tags: [python/pip, beginner/environment]
---

# pip 包管理器

## 一句话理解

pip 是 Python 的包安装工具。pytest、FastAPI、SQLAlchemy 等第三方库通常通过 pip 安装。

## 基本命令

```powershell
python -m pip install pytest
python -m pip show pytest
python -m pip list
python -m pip uninstall pytest
```

推荐写成 `python -m pip`，因为它明确使用当前 `python` 对应的 pip，减少“pip 装到了另一个 Python”的问题。

## 指定版本

```powershell
python -m pip install "pytest==9.0.0"
python -m pip install "pytest>=8,<10"
```

`==` 固定精确版本；`>=8,<10` 表示允许兼容范围。教材示例不依赖某个小版本，但正式项目应锁定经过测试的依赖组合。

## 依赖文件

传统项目使用 `requirements.txt`：

```text
pytest>=8,<10
pytest-cov>=5
```

安装：

```powershell
python -m pip install -r requirements.txt
```

现代项目也常在 `pyproject.toml` 中声明依赖。

## 常见错误

- 没激活虚拟环境就安装。
- 把 `pip freeze` 的所有本机工具都当项目依赖。
- 只写包名不记录版本，半年后环境无法复现。
- 从不可信来源安装同名包，产生供应链风险。

## 验证示例

```powershell
python -c "import pytest; print(pytest.__version__)"
```

如果输出版本号，说明当前解释器能找到 pytest。

## 练习与面试题

练习：在虚拟环境安装 pytest，查看其位置和版本，再卸载并验证导入失败。

面试：为什么 `python -m pip` 通常比直接执行 `pip` 更稳妥？

