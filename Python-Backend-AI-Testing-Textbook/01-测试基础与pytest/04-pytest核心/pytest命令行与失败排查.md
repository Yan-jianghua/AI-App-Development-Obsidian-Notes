---
knowledge_id: py-ai-test-pytest-cli-debugging
title: pytest 命令行与失败排查
project: Python 后端与 AI 应用测试教材
domain: pytest-core
note_type: concept
version: 1.0.0
status: current
created: 2026-09-18
updated: 2026-09-18
up: ["[[01-测试基础与pytest/00-学习导航]]"]
related:
  - "[[01-测试基础与pytest/04-pytest核心/pytest测试发现]]"
  - "[[01-测试基础与pytest/04-pytest核心/pytest mark测试标记]]"
replaces: []
source_refs: [REF-FOUNDATIONS]
tags: [pytest/cli, testing/debugging]
---

# pytest 命令行与失败排查

## 常用命令

```powershell
pytest                         # 全部测试
pytest tests/test_users.py     # 指定文件
pytest -k login                # 名称包含 login
pytest -m integration          # 指定标记
pytest -x                      # 首次失败停止
pytest --maxfail=3             # 最多三个失败
pytest -q                      # 简洁输出
pytest -vv                     # 更详细节点信息
pytest -s                      # 不捕获 stdout
pytest --lf                    # 只跑上次失败
pytest --collect-only          # 只收集不执行
```

## 输出捕获

pytest 默认捕获 print 和日志，测试失败时显示。`-s` 便于临时调试，但不应靠大量 print 代替清晰断言和日志。

## Traceback

`--tb=short` 简化堆栈，`--tb=long` 显示完整堆栈，`--tb=no` 隐藏。排查时从第一条有业务意义的错误向上看，而不是只看最后一行。

## 失败类型

- Collection Error：导入或发现阶段失败，测试未运行。
- Failed：断言或未预期异常。
- Error：常发生在 Fixture 创建/清理。
- Skipped/Xfailed：未执行或已知失败。

## 调试步骤

1. 用节点 ID 单独运行失败测试。
2. 使用 `-vv` 查看参数化值。
3. 检查 Fixture setup/teardown。
4. 固定随机种子和时间。
5. 重复运行，检查是否 Flaky。
6. 查看最小可复现输入，不要直接扩大超时。

## 退出码

0 通常表示全部需要通过的测试成功；非 0 表示失败、无测试、用法错误等。CI 利用退出码阻止合并。

## 常见错误

- 只重跑直到绿色，不调查首次失败。
- 使用 `-s` 后泄漏敏感输出。
- `-k` 选择范围过宽，误以为只跑一条。

## 练习与面试题

练习：制造一条 Fixture error、一条 assertion failure，用命令分别定位。

面试：collection error 和 test failure 有何不同？`--lf` 的用途是什么？

