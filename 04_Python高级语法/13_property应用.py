# coding:utf-8
class Money(object):
    def __init__(self):
        self.__money = 0

    def getMoney(self):
        return self.__money

    def setMoney(self, value):
        if isinstance(value, int):
            self.__money = value
        else:
            print("Error:不是整形数字")

    money = property(getMoney, setMoney)


m = Money()
m.money = 100  # 调用setMoney方法
print(m.money)  # 调用getMoney方法
