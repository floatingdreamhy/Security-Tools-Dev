import requests
import threading
from queue import Queue

# 设置目标（请确保你拥有对以下目标的测试授权！）
TARGET_URL = "192.168.100.140:80" 
# 这是一个非常经典的、用于合法渗透测试学习的靶场

# 常见的目录和文件字典（这里只列出几个，实际使用时字典会非常大）
WORDLIST = [
    "admin", "login", "index", "config", "wp-admin", 
    "dashboard", "api", "backup", "upload", "robots.txt",
    ".git", ".env", "console"
]

# 并发线程数
THREADS = 20

def scan_dir(queue):
    """
    从队列中取出目录名，拼接到目标URL后面进行探测
    """
    while not queue.empty():
        path = queue.get()
        url = f"{TARGET_URL}/{path}"
        
        try:
            # 发送 HTTP GET 请求，设置3秒超时
            response = requests.get(url, timeout=3)
            
            # 过滤掉常见的 404 错误页面和 302 重定向
            if response.status_code in [200, 301, 403, 405]:
                print(f"[+] Found: {url} (Status Code: {response.status_code})")
                
        except requests.exceptions.RequestException:
            # 遇到连接失败等异常直接跳过，防止程序崩溃
            pass
        
        # 标记该任务已完成
        queue.task_done()

def main():
    # 创建一个队列，将所有待扫描的目录名放入其中
    queue = Queue()
    for word in WORDLIST:
        queue.put(word)
    
    print(f"[*] Starting directory scan on: {TARGET_URL}")
    print("-" * 40)
    
    # 启动多线程进行扫描
    thread_list = []
    for _ in range(THREADS):
        t = threading.Thread(target=scan_dir, args=(queue,))
        t.start()
        thread_list.append(t)
        
    # 等待所有线程完成任务
    for t in thread_list:
        t.join()
        
    print("-" * 40)
    print("[*] Directory scanning completed.")

if __name__ == "__main__":
    main()
