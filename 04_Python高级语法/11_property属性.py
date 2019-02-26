# coding:utf-8
# class Foo(object):
#
#     def func(self):
#         print("调用实例方法")
#
#     @property
#     def prop(self):
#         return "调用property属性"
#
#
# foo = Foo()
#
# # 调用实例方法
# foo.func()
#
# # 调用property属性
# print(foo.prop)


# class Pager(object):
#
#     def __init__(self, current_page):
#         self.current_page = current_page
#         self.per_items = 10
#
#     @property
#     def start(self):
#         val = (self.current_page - 1) * self.per_items
#         return val
#
#     @property
#     def end(self):
#         val = self.current_page * self.per_items
#         return val
#
#
# p = Pager(10)
# print(p.start)
# print(p.end)


# class Goods(object):
#
#     @property
#     def price(self):
#         print("property")
#
#     @price.setter
#     def price(self, value):
#         print("price.setter")
#
#     @price.deleter
#     def price(self):
#         print("price.deleter")
#
#
# good = Goods()
# print(good.price)
# good.price = 100
# del good.price


class Goods(object):

    def __init__(self):
        # 原价
        self.original_price = 100
        # 折扣
        self.count = 0.8

    @property
    def price(self):
        # 实际价格=原价*折扣
        new_price = self.original_price * self.count
        return new_price

    @price.setter
    def price(self, value):
        self.original_price = value

    @price.deleter
    def price(self):
        del self.original_price


good = Goods()
print(good.price)
good.price = 200
print(good.price)
del good.price

