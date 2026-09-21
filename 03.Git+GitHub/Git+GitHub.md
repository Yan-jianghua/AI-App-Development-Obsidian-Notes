# Git 与 GitHub 学习导航

> Git 是分布式版本控制工具，GitHub 是托管 Git 仓库并提供协作功能的平台。两者有关联，但不是同一个东西。

## 推荐学习顺序

1. [[00.Git环境配置]]
2. [[00.Git核心概念]]
3. [[00.本地仓库基本操作]]
4. [[00.查看历史与差异]]
5. [[00.分支 合并 冲突]]
6. [[00.远程仓库]]
7. [[00.GitHub认证与连接]]
8. [[00.GitHub协作]]
9. [[00.撤销与恢复]]
10. [[00.暂存 标签 版本发布]]
11. [[00.团队规范与安全]]
12. [[00.GitHub Actions入门]]
13. [[00.Git进阶工具]]

官方文档入口：[[官方参考资料]]

## 必须先掌握的最小闭环

```text
修改文件
   ↓
git status
   ↓
git diff
   ↓
git add
   ↓
git commit
   ↓
git push
```

只要先掌握这个闭环，就能完成日常版本保存。之后再学习分支、合并、Pull Request 和撤销操作。

## 高频命令速查

```bash
git status
git add <文件>
git add .
git commit -m "说明"
git log --oneline --graph --all
git switch -c feature/login
git switch main
git merge feature/login
git pull --ff-only
git push
```

## 学习原则

- 每次操作前先执行 `git status`。
- 撤销前先确认修改位于工作区、暂存区还是提交历史。
- 不熟悉 `reset --hard` 和强制推送时不要使用。
- 提交要小而完整，一次提交只表达一个清晰意图。
- 密钥、密码、Token 和 `.env` 文件不能提交。

### 一句话记忆

> Git 管版本，GitHub 管托管与协作；先会本地提交，再学远程协作。
