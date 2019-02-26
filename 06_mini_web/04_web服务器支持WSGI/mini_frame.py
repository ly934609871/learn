# coding:utf-8
def index():
    return "主页"


def login():
    return "登录页"


def application(environ, start_response):
    start_response("200 OK", [("Content-Type", "text/html;charset=utf-8")])
    file_name = environ["PATH_INFO"]
    if file_name == "/index.py":
        return index()
    elif file_name == "/login.py":
        return login()
    else:
        return "hello python  你好啊小老弟"

