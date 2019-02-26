# coding:utf-8
import socket


def send_msg(udp_socket):
    """发送数据"""
    # 对方的ip和port
    dest_ip = input("请输入对方的ip:")
    dest_port = int(input("请输入对方的port:"))

    # 发送的数据内容
    send_data = input("请输入要发送的数据:")

    # 发送数据
    udp_socket.sendto(send_data.encode("utf-8"), (dest_ip, dest_port))


def recv_msg(udp_socket):
    """接收数据"""
    # 接收数据
    recv_data = udp_socket.recvfrom(1024)

    #
    recv_message = recv_data[0]
    send_addr = recv_data[1]

    # 打印接收到的数据
    print("%s:%s" % (str(recv_message.decode("utf-8")), send_addr))


def main():
    # 创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 绑定本地信息
    udp_socket.bind(("", 6789))

    # 循环进行发送和接收
    while True:
        print("-----udp聊天器-----")
        print("1:发送消息")
        print("2:接收消息")
        print("0:退出系统")
        option = input("请输入您的选择:")
        if option == "1":
            # 发送数据
            send_msg(udp_socket)
        elif option == "2":
            # 接收数据
            recv_msg(udp_socket)
        elif option == "0":
            break
        else:
            print("输入有误，请重新输入：")

    # 关闭套接字
    udp_socket.close()


if __name__ == "__main__":
    main()