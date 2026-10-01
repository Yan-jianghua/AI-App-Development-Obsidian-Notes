# LangChain + Agent + LangGraph 学习导航

## 独立关键词笔记

- [[09.LangChain + Agent + LangGraph/1.框架定位与基础组件/001.何时不需要Agent|何时不需要Agent]]
- [[09.LangChain + Agent + LangGraph/2.Agent与工具设计/001.工具Schema与最小权限|工具Schema与最小权限]]
- [[09.LangChain + Agent + LangGraph/2.Agent与工具设计/002.计划与停止条件|计划与停止条件]]
- [[09.LangChain + Agent + LangGraph/3.LangGraph状态与工作流/001.State与Reducer|State与Reducer]]
- [[09.LangChain + Agent + LangGraph/3.LangGraph状态与工作流/002.节点边与条件路由|节点边与条件路由]]
- [[09.LangChain + Agent + LangGraph/4.记忆 持久化与人工审批/001.Checkpoint与线程状态|Checkpoint与线程状态]]
- [[09.LangChain + Agent + LangGraph/4.记忆 持久化与人工审批/002.人工审批与中断|人工审批与中断]]
- [[09.LangChain + Agent + LangGraph/5.生产安全与评测/001.Agent轨迹评测|Agent轨迹评测]]
- [[09.LangChain + Agent + LangGraph/5.生产安全与评测/002.多Agent协作边界|多Agent协作边界]]

先理解不依赖框架的模型、工具、状态与控制流，再使用框架。简单的“提问 → 检索 → 回答”通常用普通函数即可；需要多步骤、分支、人工审批或可恢复执行时，再引入 Agent/图编排。

## 推荐顺序

1. [[00.框架定位与基础组件]]
2. [[00.Agent与工具设计]]
3. [[00.LangGraph状态与工作流]]
4. [[00.记忆 持久化与人工审批]]
5. [[00.生产安全与评测]]

LangChain 提供模型、工具、检索和 Agent 集成；LangGraph 侧重有状态编排、持久化与人工介入。框架版本变化快，代码示例应按项目锁定版本核对 [官方文档](https://docs.langchain.com/oss/python/learn)。

## 综合练习与验收

把“搜集资料 → 核查来源 → 草拟报告 → 人工审批 → 发布”画成状态图，再实现只读检索工具和一个需要审批的写入工具。为每次运行保存状态版本、工具输入输出和预算。分别在工具执行前、执行后但保存状态前、审批等待中模拟进程终止。验收时恢复执行不能重复产生写入副作用，拒绝审批不能继续发布，超出步数或成本预算必须结束并给出可恢复状态。
