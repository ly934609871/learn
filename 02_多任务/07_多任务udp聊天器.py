# coding:utf-8

import socket
import threading


def send_msg(udp_socket):
    """发送消息"""

    # while True 循环发送
    while True:
        # 输入要发送的消息
        send_data = input("请输入您要发送的信息:")

        # 接收方的ip和port
        dest_ip = input("请输入对方ip:")
        dest_port = int(input("请输入对方port:"))

        # 发送消息
        udp_socket.sendto(send_data.encode("utf-8"), (dest_ip, dest_port))


def recv_msg(udp_socket):
    """接收消息"""

    while True:
        # 接收消息
        recv_data = udp_socket.recvfrom(1024).decode("utf-8")

        # 显示接收到的消息
        print(recv_data)


def main():

    # 创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 绑定本地信息
    udp_socket.bind(("", 8000))

    # 创建子线程
    t_recv = threading.Thread(target=recv_msg, args=(udp_socket,))
    t_send = threading.Thread(target=send_msg, args=(udp_socket,))
    t_recv.start()
    t_send.start()


if __name__ == "__main__":
    main()