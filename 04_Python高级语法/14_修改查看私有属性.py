# coding:utf-8
class Test(object):
    def __init__(self, name):
        self.__name = name


a = Test("张三")
# print(a.__name)
print(a._Test__name)
