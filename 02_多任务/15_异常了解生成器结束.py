# coding:utf-8

def create_num(all_num):

    a, b = 0, 1
    current_num = 0

    while current_num < all_num:
        yield a
        a, b = b, a+b
        current_num += 1

    return "-----finish-----"


obj = create_num(10)

while True:
    try:
        result = next(obj)
        print(result)
    except Exception as result:
        print(result.value)
        break
