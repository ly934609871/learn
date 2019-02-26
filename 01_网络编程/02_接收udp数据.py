# coding:utf-8
import socket


def main():
    # 创建套接字
    udp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 绑定本地信息 必须绑定自己电脑的ip以及port
    local_addr = ("", 7899)
    udp_server_socket.bind(local_addr)

    # while True 循环接收
    while True:
        # 接收数据  1024表示本次接收的最大字节数
        recv_data = udp_server_socket.recvfrom(1024)

        # recv_data中存储的是一个元祖(接收到的数据, (发送方的ip,port))
        recv_msg = recv_data[0]  # 存储接收到的数据
        send_addr = recv_data[1]  # 存储发送方的地址信息
        # 打印接收到的数据
        # print(recv_data)
        # 使用decode进行解码
        # print("%s:%s" % (send_addr, recv_msg.decode("utf-8")))
        print("%s:%s" % (str(send_addr), recv_msg.decode("utf-8")))

    # 关闭套接字
    udp_server_socket.close()


if __name__ == "__main__":
    main()