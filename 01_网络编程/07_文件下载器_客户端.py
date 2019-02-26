# coding:utf-8
import socket


def main():

    # 创建套接字
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 服务器ip和port
    server_ip = input("请输入服务器ip:")
    server_port = int(input("请输入服务器port:"))

    # 连接服务器
    tcp_socket.connect((server_ip, server_port))

    # 输入要下载的文件名
    file_name = input("请输入要下载的文件名:")

    # 客户端发送下载请求
    tcp_socket.send(file_name.encode("utf-8"))

    # 接收服务器发送过来的数据
    recv_data = tcp_socket.recv(1024)

    # 如果存在这个文件，进行传输
    if recv_data:
        with open("[附件]"+file_name, 'wb') as f:
            f.write(recv_data)

    # 如果没有这个文件
    else:
        print("找不到文件资源")

    # 关闭套接字
    tcp_socket.close()


if __name__ == "__main__":
    main()