# coding:utf-8

import socket


def send_file_2_client(new_client_socket, new_addr):

    # 接收客户端要下载的文件名
    file_name = new_client_socket.recv(1024).decode("utf-8")
    print("客户端(%s)需要下载的文件是%s" % (str(new_addr), file_name))

    # 读取文件内容前设置内容为空
    file_content = None

    # 打开要下载的文件
    try:
        f = open(file_name, "rb")
        file_content = f.read()
        f.close()
    except Exception as result:
        print("没有要下载的文件%s" % file_name)

    # 如果文件内容不为空  发送
    if file_content:
        # 发送文件给客户端
        new_client_socket.send(file_content)


def main():
    # 创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 绑定本地信息
    tcp_server_socket.bind(("", 7890))

    # 监听套接字
    tcp_server_socket.listen(128)

    # 为多个客户端服务
    while True:
        # 等待客户端的连接
        new_client_socket, new_addr = tcp_server_socket.accept()

        # 接收客户端要下载的文件名
        file_name = new_client_socket.recv(1024).decode("utf-8")
        print("客户端(%s)需要下载的文件是%s" % (str(new_addr), file_name))

        # 调用函数进行下载,完成为客户端服务
        send_file_2_client(new_client_socket, new_addr)

        # 关闭套接字
        new_client_socket.close()

    tcp_server_socket.close()


if __name__ == "__main__":
    main()