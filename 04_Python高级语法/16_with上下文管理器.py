# coding:utf-8

# 方法一


# class File(object):
#
#     def __init__(self, filename, mode):
#         self.filename = filename
#         self.mode = mode
#
#     def __enter__(self):
#         print("Entering...")
#         self.f = open(self.filename, self.mode)
#         return self.f
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print("Exiting...")
#         self.f.close()
#
#
# with File("hello.txt", "w") as f:
#     print("writing...")
#     f.write("hello python, hello world")



# 方法二  上下文管理器库


from contextlib import contextmanager


@contextmanager
def open_file(path, mode):
    f = open(path, mode)
    yield f
    f.close()


with open_file("python.txt", "w") as f:
    f.write("python是一种面向对象的编程语言")
