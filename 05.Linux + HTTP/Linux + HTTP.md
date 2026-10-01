# Linux + HTTP 学习导航

## 独立关键词笔记

- [[05.Linux + HTTP/1.Linux命令行基础/001.文件权限与服务账号|文件权限与服务账号]]
- [[05.Linux + HTTP/2.进程与服务运维/001.进程信号与优雅停机|进程信号与优雅停机]]
- [[05.Linux + HTTP/3.网络基础/001.DNS与TLS|DNS与TLS]]
- [[05.Linux + HTTP/4.HTTP核心/001.HTTP方法与状态码|HTTP方法与状态码]]
- [[05.Linux + HTTP/4.HTTP核心/002.超时与连接池|超时与连接池]]
- [[05.Linux + HTTP/5.API通信与安全/001.CORS与CSRF|CORS与CSRF]]

Linux 是后端程序运行的环境，HTTP 是前后端、模型服务和第三方 API 交流的协议。本章目标不是背命令，而是能独立完成“登录服务器 → 定位文件与进程 → 查看日志 → 调用接口 → 判断故障在哪一层”。

## 推荐顺序

1. [[00.Linux命令行基础]]：目录、文件、管道、文本处理和权限。
2. [[00.进程与服务运维]]：进程、端口、环境变量、日志和 systemd。
3. [[00.网络基础]]：IP、端口、DNS、TCP、TLS 与常用排障工具。
4. [[00.HTTP核心]]：请求响应、方法、状态码、Header、缓存与 Cookie。
5. [[00.API通信与安全]]：JSON、认证、CORS、SSE、WebSocket 和超时重试。

## 最小排障链路

```text
域名能否解析 → TCP 端口能否连接 → TLS 是否成功 → HTTP 状态码
→ 响应体是否符合约定 → 服务日志 → 依赖服务日志
```

不要只看“网页打不开”。先把问题归类为 DNS、网络、证书、反向代理、应用、数据库或业务数据，排查速度会快很多。

## 学完应能做到

- 安全地操作 Linux 文件、权限、进程和服务。
- 用 `curl` 复现 HTTP 请求，解释常见状态码和 Header。
- 区分连接超时、读取超时、4xx、5xx 与业务错误。
- 看懂 Nginx/应用日志，使用请求 ID 串起一次调用。
- 解释 HTTPS、Cookie、Token、CORS 的边界，避免泄露密钥。

官方资料：[GNU Bash](https://www.gnu.org/software/bash/manual/)、[MDN HTTP](https://developer.mozilla.org/docs/Web/HTTP)、[curl](https://curl.se/docs/)。

## 综合练习与验收

在本机或隔离服务器运行一个只提供 `/health` 和 `/items/{id}` 的 API。先用 `curl` 记录正常请求的状态码、响应头和请求 ID，再依次制造错误域名、关闭服务、错误证书、无效令牌和不存在的资源。每次写下故障发生在 DNS、TCP、TLS、HTTP 还是业务层，并从服务日志找到同一请求。验收时应能解释 401、403、404、429、502、503、504 的区别，以及超时后为何不能盲目重发写请求。
