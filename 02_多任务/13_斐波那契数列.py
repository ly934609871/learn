# coding:utf-8


# 方法一
# numbers = list()
#
# a = 0
# b = 1
# i = 0
# while i < 10:
#     numbers.append(a)
#     a, b = b, a+b
#     i += 1
#
# for number in numbers:
#     print(number)



# 方法2 迭代器
class Fibonacci(object):

    def __init__(self, all_numbers):
        self.all_numbers = all_numbers
        self.current_number = 0
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_number < self.all_numbers:
            result = self.a

            self.a, self.b = self.b, self.a + self.b
            self.current_number += 1

            return result
        else:
            raise StopIteration


fibonacci = Fibonacci(10)

for number in fibonacci:
    print(number)

