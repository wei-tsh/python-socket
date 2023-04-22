from socket import *
import threading

def thread_func(conn):
    BUFSIZE = 1024
    rec = conn.recv(BUFSIZE)
    data = rec.decode()
    if len(data) == 0:
        conn.close()
        return
    
    conn.send('Hello World!'.encode())
    conn.close()
    return

def multithreading_server_BIO(ip: str, port: int):
    # 创建服务器套接字，使用IPv4协议，TCP协议
    serverSocket = socket(AF_INET, SOCK_STREAM)
    # 绑定端口号和套接字
    serverSocket.bind((ip, port))
    # 开启监听，设置1024个连接缓冲，暂时将连接挂起
    serverSocket.listen(1024)
    print('The server is ready to receive')
    while True:
        # 等待接受客户端的连接
        conn, addr = serverSocket.accept()
        # print(addr)
        # 创建线程
        thread = threading.Thread(target=thread_func,args=(conn,))
        thread.start()
        
    serverSocket.close()


if __name__ == '__main__':
    # 服务器端口号
    serverPort = 12000
    multithreading_server_BIO('', serverPort)
