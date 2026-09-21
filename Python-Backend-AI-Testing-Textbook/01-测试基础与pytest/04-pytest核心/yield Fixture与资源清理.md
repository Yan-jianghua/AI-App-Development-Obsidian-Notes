---
knowledge_id: py-ai-test-yield-fixture-cleanup
title: yield Fixture 与资源清理
project: Python 后端与 AI 应用测试教材
domain: pytest-core
note_type: concept
version: 1.0.0
status: current
created: 2026-09-18
updated: 2026-09-18
up: ["[[01-测试基础与pytest/00-学习导航]]"]
related:
  - "[[01-测试基础与pytest/04-pytest核心/pytest Fixture]]"
  - "[[01-测试基础与pytest/04-pytest核心/Fixture作用域]]"
replaces: []
source_refs: [REF-FOUNDATIONS]
tags: [pytest/yield-fixture, testing/cleanup]
---

# yield Fixture 与资源清理

## 核心结构

`yield` 之前负责创建资源并把它提供给测试，`yield` 之后负责清理。即使测试断言失败，pytest 仍会执行清理。

```python
@pytest.fixture
def text_file(tmp_path):
    path = tmp_path / "data.txt"
    path.write_text("hello", encoding="utf-8")
    yield path
    if path.exists():
        path.unlink()
```

执行顺序：创建文件→把 `path` 传给测试→测试完成或失败→删除文件。

## 为什么不能在测试结尾清理

```python
def test_something():
    resource = create_resource()
    assert use(resource) == "ok"
    delete_resource(resource)
```

若 assert 失败，删除不会运行。资源可能污染后续测试。Fixture teardown 能避免这种情况。

## 多个资源的清理顺序

Fixture 依赖像堆栈一样反向清理：后创建的先释放。这适合“先启动容器，再开连接；先关连接，再停容器”。

## 创建阶段失败

如果在 `yield` 前创建多个资源后中途失败，尚未进入 yield 的清理代码可能无法执行。最好把资源拆为多个小 Fixture，或使用 `try/finally`/`ExitStack` 管理部分创建。

## 清理应幂等

资源可能已被测试删除，因此清理要容忍“不存在”，但不能吞掉所有异常。清理失败会影响测试环境，应报告。

## 常见错误

- 使用 `return` 后又写清理代码，永远不会执行。
- yield 两次；Fixture 只能产生一次资源。
- 清理真实生产资源。
- teardown 吞掉重要异常。

## 练习与面试题

练习：为临时用户写 yield Fixture，测试失败后仍从仓库删除用户。

面试：为什么拆成多个小 Fixture 能改善创建中途失败的清理？

