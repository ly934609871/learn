# coding:utf-8
import socket


def main():

    # 1.创建tcp套接字
    tcp_socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2.目的ip、目的port
    server_ip = input("请输入服务器ip:")
    server_port = int(input("请输入服务器port:"))

    # 3.连接服务器
    tcp_socket_client.connect((server_ip, server_port))

    # 输入要发送的数据
    send_data = input("请输入您要发送的数据:")

    # 发送数据
    tcp_socket_client.send(send_data.encode("utf-8"))

    # 接收数据 最大接收为1024字节
    recv_data = tcp_socket_client.recv(1024)
    print("接收到的数据是:%s" % recv_data.decode("utf-8"))

    # 关闭套接字
    tcp_socket_client.close()


if __name__ == "__main__":
    main()
