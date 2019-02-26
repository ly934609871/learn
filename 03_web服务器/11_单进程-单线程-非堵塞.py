# coding:utf-8
import socket
import time


# 创建套接字
tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定
tcp_server_socket.bind(("", 9000))

# 监听
tcp_server_socket.listen(128)

# 设置套接字为非堵塞的方式
tcp_server_socket.setblocking(False)

client_socket_list = list()

while True:

    time.sleep(1)

    try:
        new_socket, new_addr = tcp_server_socket.accept()

    except Exception as result:
        print("没有新的客户端的到来")

    else:
        print("有新的客户端到来")
        new_socket.setblocking(False)  # 套接字设置为非堵塞的方式
        client_socket_list.append(new_socket)

    for client_socket in client_socket_list:

        try:
            recv_data = new_socket.recv(1024).decode("utf-8")

        except Exception as result:
            print("这个客户端没有发送数据过来")

        else:
            if recv_data:
                print("这个客户端发送数据过来了")
            else:
                # 对方调用了close 导致recv返回
                client_socket_list.remove(client_socket)
                client_socket.close()
                print("客户端已经关闭")


