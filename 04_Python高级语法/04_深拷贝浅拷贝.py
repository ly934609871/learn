# coding:utf-8
# import copy
#
# a = [11, 22]
# # 浅拷贝
# b = a
# # 深拷贝
# c = copy.deepcopy(a)
# # print(id(a))
# # print(id(b))
# # print(id(c))
# a.append(33)
# print(a)
# print(c)


# import copy
#
# a = [11, 22]
# b = [33, 44]
# c = [a, b]
# d = copy.deepcopy(c)
# e = copy.copy(c)
# b.append(55)
# print(c)
# print(d)
# print(e)
# print(id(a))
# print(id(d[0]))


import copy

a = [11, 22]
b = [33, 44]
c = (a, b)
d = copy.copy(c)
e = copy.deepcopy(c)
b.append(55)
print(c)
print(d)
print(e)