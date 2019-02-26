import threading

# 子线程死循环
def test():
    while True:
        pass

t = threading.Thread(target=test)
t.start()

# 主线程死循环
while True:
    pass

