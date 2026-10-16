import socket
import threading

# 锁定器，用于控制并发打印
print_lock = threading.Lock()

def port_scan(port):
    """
    简单的端口扫描函数
    """
    try:
        # 创建 socket 对象
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5) # 设置超时时间为0.5秒，防止无响应端口卡住
        
        # 尝试连接目标端口
        result = s.connect_ex(('127.0.0.1', port))
        
        # 如果结果为 0，说明端口是开放的
        if result == 0:
            with print_lock:
                print(f"Port {port}: Open")
        
        # 关闭连接
        s.close()
        
    except Exception as e:
        pass

def main():
    print("Starting port scanner on 127.0.0.1...")
    print("-" * 30)
    
    # 扫描 1 到 1024 号常用端口
    # 使用多线程加快扫描速度
    threads = []
    for port in range(1, 1025):
        t = threading.Thread(target=port_scan, args=(port,))
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()
    
    print("-" * 30)
    print("Port scanning completed.")

if __name__ == "__main__":
    main()
