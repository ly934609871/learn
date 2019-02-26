# coding:utf-8
# class Foo(object):
#
#     def get_bar(self):
#         return "你好"
#
#     BAR = property(get_bar)
#
#
# obj = Foo()
# result = obj.BAR
# print(result)


class Foo(object):

    def get_bar(self):
        print("getter...")
        return "你好"

    def set_bar(self, value):
        """必须两个参数"""
        print("setter...")
        return "self.value" + value

    def del_bar(self):
        print("deleter...")
        return "来了小老弟"

    BAR = property(get_bar, set_bar, del_bar, "注释...")


obj = Foo()

obj.BAR  # 自动调用第一个参数中定义的方法:get_bar
obj.BAR = "Alex"  # 自动调用第二个参数中定义的方法:set_bar,并将Alex当做参数传入
desc = Foo.BAR.__doc__  # 自动获取第四个参数的值:"注释..."
print(desc)
del obj.BAR  # 自动调用第三个参数中定义的方法:del_bar

