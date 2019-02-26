# coding:utf-8
import time


def login():
    return "welcome to our website %s" % time.ctime()


def register():
    return "-----register----- %s" % time.ctime()


def profile():
    return "-----profile----- %s" % time.ctime()


def application(file_name):
    # 如果请求是login,返回login页面
    if file_name == "/login.py":
        return login()
    # 如果请求是register,返回register页面
    elif file_name == "/register.py":
        return register()
    # 如果请求是profile,返回profile页面
    elif file_name == "/profile.py":
        return profile()
    # 如果都不是，返回can not found your page
    else:
        return "can not found your page"
