# # coding:utf-8
import socket
import re
import multiprocessing
import sys


class WSGIServer(object):

    def __init__(self, port, app):

        # 创建套接字
        self.tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # 绑定本地信息
        self.tcp_server_socket.bind(("", port))

        # 监听套接字
        self.tcp_server_socket.listen(128)

        self.application = app

    def server_client(self, new_socket):
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
        file_name = ""
        result = re.match(r"[^/]+(/[^ ]*)", request_lines[0])
        if result:
            file_name = result.group(1)
            if file_name == "/":
                file_name = "/index.html"
            print("**"*30, file_name)
            print("")

        # 如果不是以.py结尾的，认为是静态资源的请求  html/css/js/png/jpg等
        if not file_name.endswith(".py"):
            try:
                f = open("./static" + file_name, "rb")
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

        else:
            # 如果是以.py结尾的，则认为是动态资源的请求
            # WSGI协议 参数是一个字典，一个方法  在这里是set_response_header方法（方法中返回的是header的信息）
            # 字典中存储的是file_name,浏览器请求什么就返回什么
            environ = dict()
            environ["PATH_INFO"] = file_name
            body = self.application(environ, self.set_response_header)
            header = "HTTP/1.1 %s\r\n" % self.status
            for temp in self.response_header:
                header += "%s:%s\r\n" % (temp[0], temp[1])

            header += "\r\n"
            response = header + body
            # 发送response发送给浏览器
            new_socket.send(response.encode("utf-8"))

        # 关闭套接字
        new_socket.close()

    def set_response_header(self, status, response_header):
        self.status = status
        self.response_header = [("Server", "mini_web v1.0")]
        self.response_header += response_header

    def run_forever(self):

        # 为客户端服务
        while True:

            new_socket, new_addr = self.tcp_server_socket.accept()

            # 为客户端服务  多任务
            p = multiprocessing.Process(target=self.server_client, args=(new_socket,))
            p.start()

            #
            new_socket.close()

        # 关闭套接字
        self.tcp_server_socket.close()


def main():
    """控制整体，创建一个web服务器对象，然后调用这个对象的run_forever方法运行"""
    if len(sys.argv) == 3:
        try:
            port = int(sys.argv[1])  # 7890
            frame_app_name = sys.argv[2]  # mini_frame:application
        except Exception as ret:
            print("端口输入错误")
            return
    else:
        print("请按照如下标准输入")
        print("python xxx.py 7890 mini_frame:application")
        return

    # mini_frame:application
    result = re.match(r"([^:]+):(.*)", frame_app_name)
    if result:
        frame_name = result.group(1)
        app_name = result.group(2)
    else:
        print("请按照如下标准输入")
        print("python xxx.py 7890 mini_frame:application")
        return

    sys.path.append("./dynamic")

    # import frame_name  会导入frame_name.py这个模块
    frame = __import__(frame_name)  # 返回值标记着导入的这个模块
    app = getattr(frame, app_name)  # 此时app就指向了dynamic下的mini_frame模块中的application函数

    wsgi_server = WSGIServer(port, app)
    wsgi_server.run_forever()


if __name__ == "__main__":
    main()

