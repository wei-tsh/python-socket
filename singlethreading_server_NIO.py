from socket import *

def singlethreading_server_BIO(ip: str, port: str):
    # 创建服务器套接字，使用IPv4协议，TCP协议
    serverSocket = socket(AF_INET, SOCK_STREAM)
    # 绑定端口号和套接字
    serverSocket.bind((ip, port))
    # 设置等待连接为非阻塞
    serverSocket.setblocking(False)
    # 开启监听，设置x个连接缓冲
    serverSocket.listen(1024)
    # 连接列表
    conn_list = []
    print('The server is ready to receive')
    while True:
        try:
            # setblocking被设置为非阻塞IO，收不到时会报异常
            conn, addr = serverSocket.accept()
            # 设置连接非阻塞
            conn.setblocking(False)
            # 将连接放入数组
            conn_list.append(conn)
        except BlockingIOError as e:
            pass
        # 迭代每个连接，处理每个连接
        for con in conn_list:
            try:
                data = con.recv(1024).decode()

                if len(data) == 0:
                    continue
                else:
                    con.send(data.upper().encode())
                    con.close()
                    conn_list.remove(con)
            except:
                pass

if __name__ == '__main__':
    # 服务器端口号
    serverPort = 12000
    singlethreading_server_BIO('', serverPort)
