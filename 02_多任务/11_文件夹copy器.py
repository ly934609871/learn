# coding:utf-8
import os
from multiprocessing import Pool, Manager


def copy_file(q, file_name, old_folder_name, new_folder_name):
    # 打开旧文件夹
    old_file = open(old_folder_name + "/"+file_name, "rb")

    # 读取旧文件内容
    content = old_file.read()
    old_file.close()

    # 创建新文件 将旧文件内容保存在新文件中
    new_file = open(new_folder_name + "/" + file_name, "wb")
    new_file.write(content)
    new_file.close()

    # 将文件名字写入队列中
    q.put(file_name)


def main():

    # 输入需要copy的文件夹的名字
    old_folder_name = input("请输入需要copy的文件夹名字:")

    # 创建一个新的文件夹
    # 避免重复创建
    try:
        new_folder_name = old_folder_name + "[复件]"
        os.mkdir(new_folder_name)
    except:
        pass

    # 获取旧文件夹中的文件名字 listdir()
    file_names = os.listdir(old_folder_name)
    print(file_names)

    # 创建进程池
    pool = Pool(3)

    # 创建队列
    q = Manager().Queue()

    for file_name in file_names:
        pool.apply_async(copy_file, args=(q, file_name, old_folder_name, new_folder_name))

    pool.close()
    # pool.join()

    # 添加下载进度
    # 测一下文件数量
    all_file_num = len(file_names)
    copy_finish_num = 0
    while True:
        file_name = q.get()
        copy_finish_num += 1
        print("拷贝的进度是%.2f%%" % (copy_finish_num*100 / all_file_num))

        if copy_finish_num >= all_file_num:
            break

if __name__ == "__main__":
    main()
