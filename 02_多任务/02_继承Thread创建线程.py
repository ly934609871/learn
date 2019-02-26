# coding:utf-8

import threading
import time


class MyThread(threading.Thread):

    # 使用继承Thread类时，必须定义run方法，调用类时，会自动调用run方法
    def run(self):
        for i in range(1, 6):
            time.sleep(1)
            msg = "I'm the "+self.name+'@'+str(i)
            print(msg)

    # 如果需要调用login或者register方法，只能再run方法内部使用self.login或者self.register
    # def login(self):
    #     pass
    #
    # def register(self):
    #     pass


if __name__ == "__main__":
    t = MyThread()
    t.start()