# coding:utf-8
import multiprocessing
from multiprocessing import Queue


def download_from_web(q):
    """下载数据"""
    # 模拟-ta = [11, 22, 33, 44]

    # 向队列中写入数据
    for temp in data:
        q.put(temp)

    print("---下载器已经下载完了数据并且已经存入到队列中---")


def analysis_data(q):
    """数据处理"""
    data_list = list()
    # 从队列中获取数据
    while True:
        data = q.get()
        data_list.append(data)
        if q.empty():
            break
    # 模拟数据处理
    print(data_list)


def main():

    # 创建队列
    q = multiprocessing.Queue()

    # 创建多进程，将队列的引用当做实参进行传递
    p1 = multiprocessing.Process(target=download_from_web, args=(q,))
    p2 = multiprocessing.Process(target=analysis_data, args=(q,))
    p1.start()
    p2.start()


if __name__ == "__main__":
    main()