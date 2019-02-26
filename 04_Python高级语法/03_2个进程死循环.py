import multiprocessing

def deadloop():
    while True:
        pass

p = multiprocessing.Process(target=deadloop)
p.start()


while True:
    pass
