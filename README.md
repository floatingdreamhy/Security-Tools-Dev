# Security-Tools-Dev

这是我个人开发的安全工具与脚本集合，用于辅助渗透测试与红队实战。

## 🛠️ 工具列表

### 1. Python 端口扫描器 (port_scanner.py)
- **功能**：基于多线程的 TCP 端口扫描器，可快速探测目标主机的开放端口。
- **技术栈**：Python `socket` 库 + `threading` 多线程。
- **用法**：`python port_scanner.py`（默认扫描 127.0.0.1 的 1-1024 端口）

### 2. Python 目录扫描器 (dir_scanner.py)
- **功能**：基于多线程的 Web 目录/文件枚举工具，用于发现隐藏后台、敏感文件等。
- **技术栈**：Python `requests` 库 + `threading` 多线程 + `Queue` 队列。
- **用法**：`python dir_scanner.py`（默认扫描 vulnweb.com 靶场）

## 🚀 后续规划
- 添加自定义目标 URL 和字典功能
- 增加服务版本探测和状态码过滤
- 扫描结果自动导出为 HTML/CSV 报告
