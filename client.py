from socket import *
import threading
import time
import random

# 线程个数
client_thread_num = 1000
# 服务器的IP地址或主机名
serverName = '127.0.0.1'
# 服务器端口号
serverPort = 12000

# 发送函数
def send(data):
    try:
        # 创建客户套接字，使用IPv4协议，TCP协议
        clientSocket = socket(AF_INET, SOCK_STREAM)
        # 三次握手，建立TCP连接，如果失败，不断尝试连接
        while clientSocket.connect((serverName, serverPort)) == 0:
            pass
        # 模拟实际应用场景，客户端与服务端建立连接后，随机睡眠几秒
        num = random.randint(0, 500)
        time.sleep(num/100)

        # 发送任意字符串
        clientSocket.sendall(data.encode())
        # 服务器处理完所有数据，并响应，否则一直阻塞在这里
        clientSocket.recv(1024)
        # 关闭socket
        clientSocket.close()
    except Exception as e:
        print(e)

if __name__ == '__main__':
    # 随意定义一些数据，用于发送
    data = 'q8e7777773yr387yrx12yeemxhy120xn120ye817mexh12emh812h345435435v45v4v43v4v433v4435v3m'
    # 线程列表
    thread_list = []
    # 创建线程
    for i in range(client_thread_num):
        t = threading.Thread(target=send, args=(data,))
        thread_list.append(t)

    # 等待线程运行，并计时
    time_start = time.time_ns()
    # 启动线程
    for t in thread_list:
        while True:
            try:
                t.start()
                break
            except Exception as e:
                pass
    # 等待线程运行结束
    for t in thread_list:
        t.join()
    # 计算运行时间
    time_end = time.time_ns()
    print('time cost: ', time_end - time_start, 'ns', (time_end - time_start) / (1e9), 's')
