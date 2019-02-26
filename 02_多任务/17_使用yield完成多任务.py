# coding:utf-8
import time


def task_1():
    while True:
        print("-----1-----")
        time.sleep(1)
        yield


def task_2():
    while True:
        print("-----2-----")
        time.sleep(1)
        yield


def main():
    t1 = task_1()
    t2 = task_2()

    # 先运行t1,当t1遇到yield时,返回while True,
    # 然后运行t2,当t2遇到yield时,再次切换到t1中，实现了交替运行，最终实现了多任务
    # 协程
    while True:
        next(t1)
        next(t2)


if __name__ == "__main__":
    main()
