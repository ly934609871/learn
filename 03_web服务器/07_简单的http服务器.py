# coding:utf-8
import socket


def server_client(new_client_socket):
    """为客户端服务"""

    # 接收浏览器的请求  即http请求
    # GET / HTTP/1.1
    request = new_client_socket.recv(1024)
    print(request)

    # 返回http格式的数据给浏览器
    # 准备发送给浏览器的数据---header    \r\n表示一个换行
    response = "HTTP/1.1 200 OK\r\n"
    response += "\r\n"
    # 准备发送给浏览器的数据---body
    response += "<h1>hello python</h1>"
    new_client_socket.send(response.encode("utf-8"))

    # 关闭套接字
    new_client_socket.close()


def main():
    """实现整体的控制"""

    # 创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 设置当服务器先close 即服务器四次挥手之后资源能够立即释放，这样就保证了下次运行程序时，可以立即绑定7890端口
    # tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # 绑定本地信息
    tcp_server_socket.bind(("", 7890))

    # 监听
    tcp_server_socket.listen(128)

    while True:

        # 等待客户连接
        new_client_socket, new_addr = tcp_server_socket.accept()
        # 为客户端服务
        server_client(new_client_socket)

    # 关闭监听套接字
    tcp_server_socket.close()


if __name__ == "__main__":
    main()
