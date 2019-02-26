# coding:utf-8

# __doc__表示类的描述
# __module__表示当前操作的对象在哪个模块
# __class__表示当前操作的对象的类是什么
# __init__  初始化方法，通过类创建对象时，会自动调用
# __del__ 当对象在内存中被释放时，自动触发执行
# __call__ 对象后面加括号,触发执行
# __dict__ 类或对象中的所有属性
# __str__ 如果类中定义了一个__str__方法,那么在打印对象时，默认输出该方法的返回值
# __getitem__、__setitem__、__delitem__ 用于索引操作，分别表示获取、设置、删除数据
# __getslice__、__setslice__、__delslice__ 用于切片操作


# class Foo(object):
#     """类的描述"""
#     def func(self):
#         pass
#
#
# print(Foo.__doc__)


# class Test(object):
#     def __init__(self, name):
#         self.name = name
#         self.age = 18
#
#
# t = Test("李四")
# print(t.name, t.age)


# class Foo(object):
#     def __init__(self):
#         print("__init__")
#
#     def __call__(self, *args, **kwargs):
#         print("__call__")
#
#
# f = Foo()  # 调用__init__方法
# f()  # 调用__call__方法


# class Foo(object):
#     def __str__(self):
#         return "hello"
#
#
# f = Foo()
# print(f)  # 默认返回__str__的返回值


# class Foo(object):
#
#     def __getitem__(self, key):
#         print('__getitem__', key)
#
#     def __setitem__(self, key, value):
#         print('__setitem__', key, value)
#
#     def __delitem__(self, key):
#         print('__delitem__', key)
#
#
# obj = Foo()
#
# result = obj['k1']      # 自动触发执行 __getitem__
# obj['k2'] = 'hello'     # 自动触发执行 __setitem__
# del obj['k1']           # 自动触发执行 __delitem__


# class Foo(object):
#
#     def __getslice__(self, i, j):
#         print('__getslice__', i, j)
#
#     def __setslice__(self, i, j, sequence):
#         print('__setslice__', i, j)
#
#     def __delslice__(self, i, j):
#         print('__delslice__', i, j)
#
#
# obj = Foo()

# obj[-1:1]                      # 自动触发执行 __getslice__
# obj[0:1] = [11, 22, 33, 44]    # 自动触发执行 __setslice__
# del obj[0:2]                   # 自动触发执行 __delslice__


