# coding:utf-8
from collections.abc import Iterable
from collections.abc import Iterator
import time


class Classmate(object):

    def __init__(self):
        self.names = list()
        self.current_num = 0

    def add(self, name):
        self.names.append(name)

    def __iter__(self):
        """如果想让一个对象是可迭代兑现，即可以使用for，必须添加__iter__方法"""
        # 返回值
        return self

    def __next__(self):
        if self.current_num < len(self.names):
            result = self.names[self.current_num]
            self.current_num += 1
            return result
        else:
            # 迭代结束时停止
            raise StopIteration


classmate = Classmate()

classmate.add("张三")
classmate.add("李四")
classmate.add("王五")

# print("判断classmate是否是可迭代对象:", isinstance(classmate, Iterable))
# classmate_iterator = iter(classmate)
# print("判断classmate_iterator是否是迭代器:", isinstance(classmate_iterator, Iterator))

for name in classmate:
    print(name)
    time.sleep(1)
