# coding:utf-8

import socket


def main():

    # 创建套接字
    tcp_socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 绑定本地信息
    tcp_socket_server.bind(("", 7890))

    # 监听
    tcp_socket_server.listen(128)

    # 等待客户端的连接  默认堵塞，客户端连接后解堵塞
    new_socket_client, client_addr = tcp_socket_server.accept()
    print(client_addr)

    # 接收客户端的发送请求
    recv_data = new_socket_client.recv(1024)
    print(recv_data)

    # 给客户端回复消息
    new_socket_client.send("hahaha".encode("utf-8"))

    # 关闭套接字
    new_socket_client.close()
    tcp_socket_server.close()


if __name__ == "__main__":
    main()

