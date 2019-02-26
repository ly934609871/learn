# coding:utf-8
import socket
import re
import select


def server_client(new_socket, request):
    """为客户端服务"""
    # 接收浏览器的请求   解码
    # request = new_socket.recv(1024).decode("utf-8")
    # print(request)
    # print(">"*100)

    # 切割成一行  列表形式
    request_lines = request.splitlines()
    # request_lines = request_lines.pop(0)
    print(request_lines)
    # print(">>>>>" * 30)

    # GET /index.html HTTP/1.1
    # get/post/put/del

    # 提取文件名
    result = re.match(r"[^/]+(/[^ ]*)", request_lines[0])
    if result:
        file_name = result.group(1)
        if file_name == "/":
            file_name = "/index.html"
        print("**" * 30, file_name)
        print("")

    try:
        f = open("./html" + file_name, "rb")

    except:
        response = "HTTP/1.1 404 NOT FOUND\r\n"
        response += "\r\n"
        response += "<h1>---file not found---</h1>"
        new_socket.send(response.encode("utf-8"))

    else:
        html_content = f.read()
        f.close()

        response_body = html_content
        response_header = "HTTP/1.1 200 OK\r\n"
        response_header += "Content_Length:%d\r\n" % len(response_body)
        response_header += "\r\n"
        response = response_header.encode("utf-8") + response_body
        # 回复浏览器需要的页面数据
        # response += "<h1>hello</h1>"

        # 将response发送给浏览器
        new_socket.send(response)

    # 关闭套接字
    new_socket.close()


def main():

    # 创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 绑定
    tcp_server_socket.bind(("", 7899))

    # 监听
    tcp_server_socket.listen(128)
    tcp_server_socket.setblocking(False)  # 把监听套接字变为非堵塞

    # 创建一个epoll对象
    epl = select.epoll()

    # 将监听套接字对应的fd注册到epoll中
    epl.register(tcp_server_socket.fileno(), select.EPOLLIN)

    fd_event_dict= dict()
    # 等待客户端的连接
    while True:

        fd_event_list = epl.poll()  # 默认堵塞，直到os监测到数据到来，通过事件通知的方式告诉这个程序，此时解堵塞

        # [(fd, event), (套接字对应的文件描述符,事件类型)]
        for fd, event in fd_event_list:
            # 等待新的客户端的连接
            if fd == tcp_server_socket.fileno():
                new_socket, new_addr = tcp_server_socket.accept()
                epl.register(new_socket.fileno(), select.EPOLLIN)
                fd_event_dict[new_socket.fileno()] = new_socket

            elif event == select.EPOLLIN:
                recv_data = fd_event_dict[fd].recv(1024).decode("utf-8")
                if recv_data:
                    server_client(fd_event_dict[fd], recv_data)
                else:
                    fd_event_dict[fd].close()
                    epl.unregister(fd)
                    del fd_event_dict[fd]

    # 关闭监听套接字
    tcp_server_socket.close()


if __name__ == "__main__":
    main()