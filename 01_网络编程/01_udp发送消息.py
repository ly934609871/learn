# coding:utf-8
import socket


def main():
    # 创建udp套接字
    udp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 绑定本地信息
    udp_server_socket.bind(("", 7890))

    # 添加 while True 可以循环发送
    while True:
        # 输入要发送的内容
        send_data = input("请输入需要发送的数据:")

        # 如果输入的数据是exit 那么退出发送
        if send_data == "exit":
            break

        # 发送数据  udp使用sendto,tcp使用send,
        # 发送的内容需要使用encode("utf-8")进行编码，如果是具体的数据可以在数据前添加字母b，转化成bytes类型
        # 元祖内部填写发送的目的ip和port
        udp_server_socket.sendto(send_data.encode("utf-8"), ("192.168.2.1", 8080))

    # 关闭套接字
    udp_server_socket.close()


if __name__ == "__main__":
    main()








