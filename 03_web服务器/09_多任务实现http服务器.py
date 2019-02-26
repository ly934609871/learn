# coding:utf-8

# 多进程
# import socket
# import re
# import multiprocessing
#
#
# def server_client(new_socket):
#     """为客户端服务"""
#     # 接收浏览器的请求   解码
#     request = new_socket.recv(1024).decode("utf-8")
#     # print(request)
#     # print(">"*100)
#
#     # 切割成一行  列表形式
#     request_lines = request.splitlines()
#     # request_lines = request_lines.pop(0)
#     print(request_lines)
#     # print(">>>>>" * 30)
#
#     # GET /index.html HTTP/1.1
#     # get/post/put/del
#
#     # 提取文件名
#     result = re.match(r"[^/]+(/[^ ]*)", request_lines[0])
#     if result:
#         file_name = result.group(1)
#         if file_name == "/":
#             file_name = "/index.html"
#         print("**"*30, file_name)
#         print("")
#
#     try:
#         f = open("./html" + file_name, "rb")
#
#     except:
#         response = "HTTP/1.1 404 NOT FOUND\r\n"
#         response += "\r\n"
#         response += "<h1>---file not found---</h1>"
#         new_socket.send(response.encode("utf-8"))
#
#     else:
#         html_content = f.read()
#         f.close()
#
#         # 回复浏览器需要的页面数据
#         # header
#         response = "HTTP/1.1 200 OK\r\n"
#         response += "\r\n"
#         # body
#         # response += "<h1>hello</h1>"
#
#         # 将response header发送给浏览器
#         new_socket.send(response.encode("utf-8"))
#         # 将response body发送给浏览器
#         new_socket.send(html_content)
#
#     # 关闭套接字
#     new_socket.close()
#
#
# def main():
#
#     # 创建套接字
#     tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
#     # 绑定本地信息
#     tcp_server_socket.bind(("", 8008))
#
#     # 监听套接字
#     tcp_server_socket.listen(128)
#
#     # 为客户端服务
#     while True:
#
#         new_socket, new_addr = tcp_server_socket.accept()
#
#         # 为客户端服务  多任务
#         p = multiprocessing.Process(target=server_client, args=(new_socket,))
#         p.start()
#
#         #
#         new_socket.close()
#
#     # 关闭套接字
#     tcp_server_socket.close()
#
#
# if __name__ == "__main__":
#     main()


# 多线程  资源共享
import socket
import re
import threading


def server_client(new_socket):
    """为客户端服务"""
    # 接收浏览器的请求   解码
    request = new_socket.recv(1024).decode("utf-8")
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
        print("**"*30, file_name)
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

        # 回复浏览器需要的页面数据
        # header
        response = "HTTP/1.1 200 OK\r\n"
        response += "\r\n"
        # body
        # response += "<h1>hello</h1>"

        # 将response header发送给浏览器
        new_socket.send(response.encode("utf-8"))
        # 将response body发送给浏览器
        new_socket.send(html_content)

    # 关闭套接字
    new_socket.close()


def main():

    # 创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 绑定本地信息
    tcp_server_socket.bind(("", 8000))

    # 监听套接字
    tcp_server_socket.listen(128)

    # 为客户端服务
    while True:

        new_socket, new_addr = tcp_server_socket.accept()

        # 为客户端服务  多任务
        t = threading.Thread(target=server_client, args=(new_socket, ))
        t.start()

        # new_socket.close()

    # 关闭套接字
    tcp_server_socket.close()


if __name__ == "__main__":
    main()