# coding:utf8
import threading
import time


def sing():
    for i in range(5):
        print("-----正在唱:你好不好------")
        time.sleep(1)


def dance():
    for i in range(10):
        print("-----正在跳舞-----")
        time.sleep(1)


def main():
    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)
    t1.start()
    t2.start()
    # 查看线程数
    while True:
        length = len(threading.enumerate())
        print(length)
        if length <= 1:
            break
        time.sleep(1)


if __name__ == "__main__":
    main()



# names = ["aa", "bb", "cc"]
# for temp in enumerate(names):
#     print(temp)