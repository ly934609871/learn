# coding:utf-8
def test1(a, b, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)
    # test2(a, b, args, kwargs)  #相当于test2(11, 22, ((33, 44, 55, 66), {"name":"老王", "age":18}))
    # test2(a, b, *args, kwargs)  # 相当于test2(11, 22, 33, 44, 55, 66, {"name":"老王", "age":18})
    test2(a, b, *args, **kwargs)  # 相当于test2(11, 22, 33, 44, 55, 66, "name":"老王", "age":18)


def test2(a, b, *args, **kwargs):
    print("-------------"*2)
    print(a)
    print(b)
    print(args)
    print(kwargs)


test1(11, 22, 33, 44, 55, 66, name="老王", age=18)
