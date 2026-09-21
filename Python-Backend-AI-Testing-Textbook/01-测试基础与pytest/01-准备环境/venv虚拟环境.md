---
knowledge_id: py-ai-test-venv
title: venv 虚拟环境
project: Python 后端与 AI 应用测试教材
domain: python-environment
note_type: concept
version: 1.0.0
status: current
created: 2026-09-18
updated: 2026-09-18
up: ["[[01-测试基础与pytest/00-学习导航]]"]
related: ["[[01-测试基础与pytest/01-准备环境/pip包管理器]]"]
replaces: []
source_refs: [REF-FOUNDATIONS]
tags: [python/venv, beginner/environment]
---

# venv 虚拟环境

## 一句话理解

虚拟环境是“只属于当前项目的 Python 和第三方包空间”。项目 A 可以使用 pytest 的一个版本，项目 B 使用另一个版本，彼此不冲突。

## 为什么初学测试就需要它

如果把所有包装到系统 Python 中，时间久了会出现版本冲突，也难以知道项目真正依赖什么。CI 服务器通常会从空环境安装依赖，所以本地也应模拟这种隔离方式。

## 创建与激活

在项目目录执行：

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

macOS/Linux 的激活命令是：

```bash
source .venv/bin/activate
```

激活后，终端前通常出现 `(.venv)`。验证：

```powershell
python -c "import sys; print(sys.executable)"
```

输出路径应该指向项目的 `.venv`。

## 退出

```powershell
deactivate
```

退出不会删除环境，只是不再使用它。

## 常见错误

- 把 `.venv` 提交到 Git：环境体积大且不可跨机器可靠复制，应加入 `.gitignore`。
- 激活后仍调用其他 Python：用 `python -c` 检查实际解释器。
- 删除环境后认为代码丢失：虚拟环境只存解释器和包，项目源码不在其中。

## 最佳实践

每个项目一个 `.venv`；依赖通过配置文件记录；环境损坏时删除并重新创建，而不是手工修补。

## 练习

创建两个目录，各自创建虚拟环境。在其中一个安装 pytest，验证另一个环境无法导入 pytest。

## 面试问题

虚拟环境解决了什么问题？为什么不应该把 `.venv` 提交到版本库？

