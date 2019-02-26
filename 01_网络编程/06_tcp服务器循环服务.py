# coding:utf-8
import socket


def main():
    # 创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 绑定本地信息
    tcp_server_socket.bind(("", 7890))

    # 监听
    tcp_server_socket.listen(128)

    # while True 可以为客户端循环服务
    while True:

        # 等待客户链接   当有客户端连接时accept解堵塞
        new_socket_client, new_addr = tcp_server_socket.accept()

        # while True 可以为一个客户端提供多次服务
        while True:

            # 接收客户端的数据   当接收到客户端发送的数据或者客户端调用close(即关闭)时，recv解堵塞
            recv_data = tcp_server_socket.recv(1024)
            print("客户端发送过来的请求是:%s" % recv_data.decode("utf-8"))

            # 如果客户端发送的数据不为空 继续服务
            if recv_data:
                # 回复客户端
                new_socket_client.send("hahahaha".encode("utf-8"))

            # 客户端发送的数据为空，即调用close时，退出服务
            else:
                break

        # 关闭套接字  已经为一个客户端服务完毕
        new_socket_client.close()


    tcp_server_socket.close()


if __name__ == "__main__":
    main()

