# coding:utf-8
# 装饰器
# def set_func(func):
#     def call_func():
#         print("---func---")
#         func()
#     return call_func
#
#
# @set_func
# def test1():
#     print("---test1---")
#
#
# test1()


# 装饰器原理
# def set_func(func):
#     def call_func():
#         print("---func---")
#         func()
#     return call_func
#
#
# def test1():
#     print("---test1---")
#
#
# result = set_func(test1)
# result()


# # 对没有参数、没有返回值的函数进行装饰
# import time
#
#
# def set_func(func):
#
#     def call_func():
#         t_start = time.time()
#         print("---func---")
#         func()
#         t_end = time.time()
#         t = t_end - t_start
#         print(t)
#     return call_func
#
#
# @set_func
# def test1():
#     print("---test1---")
#
#
# test1()


# 对有参数、无返回值的函数进行装饰
# def set_func(func):
#     def call_func(name, score):
#         print("---func---")
#         func(name, score)
#     return call_func
#
#
# @set_func
# def test1(name, score):
#     print("---test1---")
#     print("%s的期末考试成绩是%d分" % (name, score))
#
#
# test1("小明", 100)


# 对不定长参数的函数进行装饰
# def set_func(func):
#     def call_func(num, *args, **kwargs):
#         print("---func---")
#         func(num, *args, **kwargs)  # 必须写*args和**kwargs进行拆包  args和kwargs有错
#     return call_func
#
#
# @set_func
# def test(num, *args, **kwargs):
#     print("---test---%d" % num)
#     print("---test---", args)
#     print("---test---", kwargs)
#
#
# test(100, 200, 300, 400, k=500)


# 对带有返回值的函数进行装饰
# def set_func(func):
#     def call_func(num, *args, **kwargs):
#         print("---func---")
#         return func(num, *args, **kwargs)  # 必须写*args和**kwargs进行拆包  args和kwargs有错
#     return call_func
#
#
# @set_func
# def test(num, *args, **kwargs):
#     print("---test---%d" % num)
#     print("---test---", args)
#     print("---test---", kwargs)
#     return "ok"
#
#
# result = test(100)
# print(result)


# 通用装饰器
# def set_func(func):
#     def call_func(*args, **kwargs):
#         print("---func---")
#         return func()
#     return call_func
#
#
# @set_func
# def test():
#     print("---test---")
#     return "ok"
#
#
# test()


# 多个装饰器对同一个函数进行装饰
# 先装饰下面的，后装饰上面的
# 先执行上面的，后执行下面的
# def add_permission_one(func):
#     print("---开始装饰权限1---")
#     def call_func(*args, **kwargs):
#         print("---权限认证1---")
#         return func(*args, **kwargs)
#     return call_func
#
#
# def add_permission_two(func):
#     print("---开始装饰权限2---")
#     def call_func(*args, **kwargs):
#         print("---权限认证2---")
#         return func(*args, **kwargs)
#     return call_func
#
#
# @add_permission_one
# @add_permission_two
# def test(*args, **kwargs):
#     print("---test---")
#     print("---test---", args)
#     print("---test---", kwargs)
#     return "ok"
#
#
# test(1)


# def set_func_1(func):
#     def call_func():
#         return "<h1>" + func() + "</h1>"
#     return call_func
#
#
# def set_func_2(func):
#     def call_func():
#         return "<td>" + func() + "</td>"
#     return call_func
#
#
# @set_func_1
# @set_func_2
# def test():
#     return "hahaha"
#
#
# print(test())


# 用类对函数进行装饰
# class Test(object):
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, *args, **kwargs):
#         print("这里是装饰器添加的功能")
#         return self.func(*args, **kwargs)
#
#
# @Test
# def get_str():
#     return "hahaha"
#
#
# print(get_str())


# 带有参数的装饰器版本1
# def set_func(func):
#     def call_func(*args, **kwargs):
#         level = args[0]
#         if level == 1:
#             print("---权限1验证---")
#         elif level == 2:
#             print("---权限2验证---")
#         return func()
#     return call_func
#
#
# @set_func
# def test1():
#     print("---test1---")
#     return "ok1"
#
#
# @set_func
# def test2():
#     print("---test2---")
#     return "ok2"


# test1(1)
# test2(2)


# 带有参数的装饰器版本2
def set_level(level_num):
    def set_func(func):
        def call_func(*args, **kwargs):
            if level_num == 1:
                print("---权限1验证---")
            elif level_num == 2:
                print("---权限2验证---")
            return func()
        return call_func
    return set_func


@set_level(1)
def test1():
    print("---test1---")
    return "ok1"


@set_level(2)
def test2():
    print("---test2---")
    return "ok2"


test1()
test2()






















































































