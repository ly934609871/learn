# coding:utf-8

# import time
# import threading
#
# g_num = 100
#
#
# def test1():
#     global g_num
#     g_num += 1
#     print("-----in test1 g_num=%d-----" % g_num)
#
#
# def test2():
#     print("-----in test2 g_num=%d-----" % g_num)
#
#
# def main():
#     t1 = threading.Thread(target=test1)
#     t2 = threading.Thread(target=test2)
#     t1.start()
#     time.sleep(1)
#     t2.start()
#     time.sleep(1)
#
#     print("-----in main Thread g_num=%d" % g_num)
#
#
# if __name__ == "__main__":
#     main()


import threading
import time


def test1(temp):
    temp.append(33)
    print("-----in test1 temp=%s" % str(temp))


def test2(temp):
    print("-----in test2 temp=%s" % str(temp))


g_nums = [11, 22]


def main():
    # target 指定这个线程去哪里执行
    # args 指定调用函数时传递什么数据过去  且必须是元祖
    t1 = threading.Thread(target=test1, args=(g_nums,))
    t2 = threading.Thread(target=test2, args=(g_nums,))
    t1.start()
    time.sleep(1)
    t2.start()
    time.sleep(1)

    print("-----in main Thread g_nums=%s" % g_nums)


if __name__ == "__main__":
    main()