# coding:utf8
# print('hello, python!')
# print('Hello, World!')
# print('hahahahah')
# print('hahahgafava xsanxsax')
# print(1.01**365)
# print("你好 "*100)

# qq_number = "934609871"
# qq_password = "ly031012"
# print(qq_number, qq_password, sep='\n')


# price = 8.5
# weight = 7.5
# money = price*weight
# money = money - 5
# print(money)


# name = '小明'
# age = 18
# gender = '男'
# height = 1.75
# weight = 75.0
# student = [name, age, gender, height, weight]
# print(student)

# first_name = '刘'
# last_name = '杨'
# print((first_name + last_name), (first_name + last_name), sep='\n')


# a = float(input())
# b = float(input())
# c = a + b
# print(c)


# a = input('请输入a:')
# b = input('请输入b:')
# print(type(a))
# print(type(b))


# qq = input("请输入您的qq号：")
# password = input("请输入您的qq密码:")
# print(qq, password, sep='\n')


# price = float(input("请输入苹果单价:"))
# weight = float(input("请输入苹果重量:"))
# print(price*weight)


# price = float(input("请输入苹果单价:"))
# weight = float(input("请输入苹果重量:"))
# money = price * weight
# print('苹果价格是%.2f' % money)


# name = str(input('请输入您的姓名:'))
# print('欢迎您，%s!' % name)
#
#
# student_number = int(input("请输入您的学号:"))
# print("您的学号是%06d" % student_number)


# price = 7.6
# weight = 3.2
# money = price * weight
# print('苹果的单价是%.2f,苹果的重量是%.2f,一共花费%.2f元。' % (price, weight, money))


# scale = float(input('请输入一个数字:'))
# print('%.2f就是%.1f%%.' % (scale, scale*100))


# age = int(input('请输入您的年龄:'))
# if age >= 18:
#     print('您是成年人，可以进入网吧！')
# elif age >= 0:
#     print('您是未成年人，禁止进入网吧！')
# else:
#     print('您输入的年龄有误，请重新输入!')


# age = int(input('请输入您的年龄:'))
# if age >= 120 or age <= 0:
#     print('年龄有误，请重新输入！')
# elif age >= 18:
#     print('您是成年人，可以进入网吧。')
# else:
#     print('您是未成年人，禁止进入网吧！')


# age = int(input('请输入您的年龄:'))
# if age >= 0 and age <= 120:
#     print('年龄正确')
# else:
#     print('年龄错误')
# print('哈哈哈，开心每一天！')


# python_score = float(input('请输入您的python成绩:'))
# c_score = float(input('请输入您的C语言成绩:'))
# if python_score >= 60 or c_score >= 60:
#     print('恭喜您，成绩合格!')
# else:
#     print('很抱歉，成绩不合格！')


# is_employee = False
# if is_employee:
#     print('欢迎您')
# if not is_employee:
#     print('禁止进入')


# holiday_name = str(input('请输入节日名称:'))
# if holiday_name == '情人节':
#     print('买玫瑰') or print('看电影')
# elif holiday_name == '平安夜':
#     print('买苹果') or print('吃大餐')
# elif holiday_name == '生日':
#     print('买蛋糕')
# else:
#     print('每天都是节日啊......')


# has_ticket = True
# knife_length = float(input('你的刀有多长：'))
#
# if has_ticket:
#     print('可以进行安检')
#     if knife_length <= 0.2:
#         print('可以上车')
#     else:
#         print('你的刀的长度为%.2f米,不可以上车.' % knife_length)
# else:
#     print('不可以进站')


#  石头剪刀布   石头（1）、剪刀（2）、布（3）
# import random
#
# #  提示玩家在控制台出拳
# player = int(input('请输入您要出的拳 石头（1）、剪刀（2）、布（3）：'))
# #  电脑随机出拳
# computer = random.randint(1, 3)
# print('玩家要出的拳头是:%d --- 电脑出的拳是:%d' % (player, computer))
#
#
# #  对玩家输入的拳进行校验
# if player > 3 or player < 1:
#     print('您输入的拳有误，请重新输入:')
#     #  玩家、机器重新出拳
#     player = int(input('请输入您要出的拳 石头（1）、剪刀（2）、布（3）：'))
#     computer = random.randint(1, 3)
#     print('玩家要出的拳头是:%d --- 电脑出的拳是:%d' % (player, computer))
#     #  比较胜负
#     #  石头胜剪刀
#     #  剪刀胜布
#     #  布胜石头
#     if (player == 1 and computer == 2) or (player == 2 and computer == 3) or (player == 3 and computer == 1):
#         print('恭喜你，胜利了！')
#     elif player == computer:
#         print('你和电脑打成了平手。')
#     else:
#         print('很抱歉，你输了。')



# i = 1
# while i <= 5:
#     print('hello,python')
#     i += 1
# print('hello,world')


# 0~100之间的数字累加
# n = 0
# sum = 0
# sum += n
# while n <= 100:
#     sum += n
#     n += 1
# print('0~100之间的数的求和结果是%d.' % sum)


# 0~100之间的偶数之和
# n = 0
# sum = 0
# while n <= 100:
#     if n % 2 == 0:
#         sum += n
#     n += 1
# print('0~100之间偶数的累加和是%d.' % sum)


# break
# i = 0
# while i < 10:
#     if i == 3:
#         break
#     print(i)
#     i += 1
# print('over')


# continue
# i = 0
# while i < 10:
#     if i == 3:
#         i += 1
#         continue
#     print(i)
#     i += 1

# i = 0
# while i < 5:
#     i += 1
#     if i == 1:
#         print('*')
#     elif i == 2:
#         print('**')
#     elif i == 3:
#         print('***')
#     elif i == 4:
#         print('****')
#     else:
#         print('*****')


# 小星星
# row = 1
# while row <= 5:
#     print('*' * row)
#     row += 1


# 九九乘法表 1
# row = 1
# while row <= 9:
#     col = 1
#     while col <= row:
#         print('%d*%d=%d   \t' % (col, row, col*row), end='')
#         col += 1
#     # print('第 %d 行' % row)
#     # 增加换行
#     print('')
#     row += 1

# 九九乘法表 2
# for i in range(1, 10):
#     for j in range(1, i+1):
#         print('{0}*{1}={2}\t'.format(j, i, i*j), end='')
#     print()

# 九九乘法表 3
# print('\n'.join(' '.join("%dx%d=%-2d" % (x, y, x*y) for x in range(1, y+1)) for y in range(1, 10)))


# 函数
# name = "小明"
#
# def say_hello():
#
#     """打招呼"""
#     print('你好！')
#     print('hello!')
#     print('aniyaseyo!')
#
# print(name)
# say_hello()
# print(name)


# def sum_2_sum(num1, num2, num3):
#     result = num1 + num2 + num3
#     print('%d+%d+%d=%d' % (num1, num2, num3, result))
# sum_2_sum(1, 2, 3)


# def sum_2_num(num1, num2):
#
#     """对两个数的求和"""
#     return num1 + num2
#
# result = sum_2_num(10, 20)
# print('计算结果是%d.' % result)


# 函数的嵌套调用
# def test1():
#     print('*' * 5)
#
# def test2():
#     print('$' * 5)
#     test1()
#     print('$' * 5)
#
# test2()


# 函数的嵌套调用
# def print_line(char, times):
#     print(char * times)
#
# def print_lines(line, char, times):
#     """打印多行分割线
#
#     :param line:分割线行数
#     :param char:分隔字符
#     :param times:每行分割字符个数
#     """
#     n = 1
#     while n <= line:
#         print_line(char, times)
#         n += 1
#
# print_lines(3, '$$$$$ ', 5)



# 列表操作
# number_list = [6, 2, 3, 7, 9, 1, 10]
# print(number_list.count(2))
# name_list = ['zhangsan', 'lisi', 'wangwu']
# number_list.sort(reverse=False)
# name_list.sort(reverse=True)
# print(number_list)
# print(name_list)

# number_list.sort(reverse=True)
# number_list[1] = 5
# number_list.append(20)
# number_list.append(16)
# number_list.insert(3, 21)
# number_list.pop()
# number_list.remove(10)
# print(name_list.clear())
# print(len(number_list))
# print(number_list.count(1))


# 列表的循环遍历
# name_list = ['zhangsan', 'lisi', 'wangwu']
# for name in name_list:
#     print(name)

# 列表可以存储不同类型的数据
# n_list = [1, 12, 'python', 'java', 'hahaha']
# print(n_list)



# 元祖
# info_tuple = ('张三', 24, 1.75, '李四', 33, 'hello', 24)
# print(info_tuple.count(24))
# print(info_tuple.index(24))
# print(info_tuple[1])
# print(len(info_tuple))


# 元祖的循环遍历
# info_tuple = ('张三', '李四', '王五', 33, 1.75)
# for item in info_tuple:
#     print(item)

# info = ('张三', 10, '四年级', 1.50)
# print('%s的年龄是%d岁,正在上%s,他的身高是%.2f米' % info)


# 列表、元祖转换
# number_list = [1, 2, 3, 4, 5, 6, 7]
# print(type(number_list))
# print(number_list)
# number_tuple = tuple(number_list)
# print(number_tuple.index(2))
# print(type(number_tuple))


# 字典
# tuple = ('xiaoming', 34)
# xiaoming = {tuple: '小明',
#             'age': 18,
#             'gender': 'male',
#             'height': 1.75}
# print(xiaoming.values())
# print(xiaoming.keys())
# print(xiaoming.items())
# print(xiaoming)


# 字典的增删改查
# xiaoming = {'name': '小明',
#             'age': 18,
#             'gender': 'male',
#             'height': 1.75}
#
# # 取
# print(xiaoming['name'])
# print(xiaoming['age'])
# print(xiaoming.keys())
# print(xiaoming.values())
# print(xiaoming.items())
#
# # 增
# xiaoming['score'] = 100
# print(xiaoming)
#
# # 改
# xiaoming['name'] = '刘杨'
# print(xiaoming)
#
# # 删
# xiaoming.pop('gender')
# print(xiaoming)
#
# # 统计长度
# print(len(xiaoming))

# 合并字典
# xiaoming_dict = {'name': '小明',
#                  'age': 18}
# temp_dict = {'height': 1.75}
# xiaoming_dict.update(temp_dict)
# print(xiaoming_dict)


# 清空字典
# xiaoming = {'name': '刘杨',
#             'age': 18}
# xiaoming.clear()
# print(xiaoming)

# 循环遍历
# xiaoming = {'qq': 934609871,
#             'password': 12345678,
#             'level': 56}
# for k in xiaoming:
#     print('%s:%s\t' % (k, xiaoming[k]))


# card_list = [
#     {'name': '刘杨',
#      'age': 24,
#      'gender': 'male'},
#     {'name': 'lisa',
#      'age': 18,
#      'gender': 'female'}
# ]
# for card_info in card_list:
#     print(card_info)


# 字符串
# str1 = "hello python"
# str2 = '科比的外号是"小飞侠"。'
#
# print(str2)
# print(str1[6])
#
# for i in str1:
#     print(i, end="")
#
# print("")
#
# for j in str2:
#     print(j, end="")


# 字符串操作
# hello_str = "Hello hello"
#
# print(len(hello_str))
# print(hello_str.count("hello"))
# print(hello_str.index("l"))


# 判断空白字符
# space_str = "      \t\n\r"
# print(space_str.isspace())


# 判断字符串中是否值包含数字

# 1>都不能判断小数
# num_str = "1.1"
# 2>unicode字符串
# num_str = "\u00b2"
# 3>中文数字
# num_str = "一千"
#
# print(num_str)
# print(num_str.isdecimal())
# print(num_str.isdigit())
# print(num_str.isnumeric())


# 字符串的查找与替换

# hello_str = "hello python"
# # 判断是否以指定的字符串开始
# print(hello_str.startswith("h"))
# # 判断是否以指定的字符串结尾
# print(hello_str.endswith("n"))
# # 查找指定字符串  返回第一个字符的索引
# print(hello_str.find("jajaj"))
# # 替换字符串
# print(hello_str.replace("python", "world"))


# 文本对齐
# poem = ["\t\n草",
#         "白居易",
#         "离离原上草\t\n",
#         "一岁一枯荣",
#         "野火烧不尽",
#         "春风吹又生"]
# for poem_str in poem:
#     print('|%s|' % poem_str.strip().center(10, " "))


# 去除空白字符
# str = "  jsjs  hshsh   "
# print(str.strip())


# 拆分字符串
# num_str = " 123 33 555  nihao 离离原上草\t"
# print(num_str.split())

# 字符串切片
# att_str = "abcdefghijklmn"
# print(att_str[0:10:2])
# print(att_str[-1])
# print(att_str[:6])
# print(att_str[2:])
# print(att_str[-2:])
# # 倒序  从最后一个字符开始向左进行切取
# print(att_str[::-1])


# dict = {"name": "liuyang",
#         "age": 18,
#         "gender": "male"}
# print(max(dict))
# print(min(dict))

# 完整的for语法
# for num in [1, 2, 3]:
#     print(num)
#     if num == 3:
#         break
# else:
#     print('会不会执行呢？')
# print('循环结束')


# 引用
# def test(num):
#     print("在函数内部%d对应的内存地址是%d" % (num, id(num)))
#
#     # 定义一个字符串变量
#     result = "hello"
#     print("函数要返回数据的内存地址是%d" % id(result))
#     # 将字符串变量返回, 返回的是数据的引用，而不是数据本身
#     return result
#
# # 1.定义一个数字的变量
# a = 10
#
# # 数据的地址本质上就是一个数字
# print("a变量保存数据的内存地址是%d" % id(a))
#
# # 2.调用test函数
# # 如果函数有返回值，但是没有定义变量接收，程序不会报错，但是无法获取返回结果
# r = test(a)
# print("%s的内存地址是%d" % (r, id(r)))


# d = {}
# print(d)
# print(id(d))
# d["name"] = "zhangsan"
# print(d)
# print(id(d))
# d["age"] = 18
# print(d)
# print(id(d))

# a = 1
# print(hash(a))
# a = "jaja"
# print(hash(a))
# a = (a,)
# print(hash(a))


# 局部变量
# def demo1():
#
#     num = 10
#     print("输出的数字是%d" % num)
#
# demo1()


# 全局变量
# num = 10
#
# def demo1():
#
#     # global关键字会告诉解释器后面的变量是全局变量，再使用赋值语句时，就不会创建局部变量
#     global num
#     num = 1
#     print("demo1==>%d" % num)
#
# def demo2():
#     print("demo2==>%d" % num)
#
# demo1()
# demo2()


# 利用元祖返回函数的多个值
# def measure():
#
#     """测量温度和湿度"""
#     print("测量开始...")
#     temp = 26
#     wet = 50
#     print("测量结束...")
#     # 元祖可以返回多个多个值
#     # return ("温度是%.1f,湿度是%.1f" % (temp, wet))
#     return temp, wet
#
# result = measure()
# print(result)
#
# # 单独处理温度或湿度  不方便
# print(result[0])
# print(result[1])
#
# # 如果函数的返回结果是元祖，同时希望单独处理元祖中的元素
# # 可以使用多个变量一次接收函数的返回结果
# # 注意：使用多个变量接收结果时，变量的个数应该与元祖中元素的数量保持一致
# gl_temp, gl_wet = measure()
# print(gl_temp)
# print(gl_wet)


# 交换数字
# a = 1
# b = 2

# 解法1  使用其他变量
# c = a
# a = b
# b = c
# print(a, b)

# 解法2   不使用其他变量
# a += b
# b = a - b
# a = a - b
# print(a, b)

# 解法3
# a, b = b, a
# print(a, b)


# 不可变和可变参数
# def demo1(num, num_list):
#     print("函数内部的代码")
#
#     # 在函数内部，针对参数进行赋值语句，不会修改到外部的实参变量
#     num = 100
#     num_list = [1, 2, 3]
#     print(num_list)
#     print(num)
#     print("函数执行完成")
#
# gl_num = 99
# gl_list = [4, 5, 6]
# demo1(gl_num, gl_list)
# print(gl_num)
# print(gl_list)


# 函数内部使用方法修改可变参数
# def demo(num_list):
#
#     print("函数内部的代码")
#     # 使用方法修改列表的内容
#     num_list.append(9)
#     print(num_list)
#     print("函数执行完成")
#
# gl_list = [1, 2, 3]
# demo(gl_list)
# print(gl_list)


# +=
# def demo(num, num_list):
#
#     print("函数内部的代码")
#
#     num += num
#
#     num_list += num_list
#
#     print(num)
#     print(num_list)
#     print("函数执行结束")
#
# gl_num = 1
# gl_list = [1, 2, 3]
# demo(gl_num, gl_list)
# print(gl_num)
# print(gl_list)


# 缺省参数
# num_list = [1, 3, 10, 2, 7, 5]
#
# num_list.sort()
# print(num_list)
#
# num_list.sort(reverse=True)
# print(num_list)



# def print_info(name, gender=True):
#     """
#
#     :param name:姓名
#     :param gender:性别  True 男生  False 女生
#     :return:
#     """
#     gender_text = "男生"
#     if not gender:
#         gender_text = "女生"
#
#     print("%s是%s" % (name, gender_text))
#
# print_info("小明", False)


# 多值参数
# def demo(num, *nums, **person):
#
#     print(num)
#     print(nums)
#     print(person)
#
# # demo(1)
# demo(1, 2, 3, 4, 5)
# demo(1, 2, 3, 4, 5, name="小明", age=18)


# 计算任意多个数字的和
# def sum_numbers(*args):
#
#     num = 0
#     for n in args:
#         num += n
#     return num
#
# print(sum_numbers(1, 2, 3, 4, 5, 6))


# 元祖和字典的拆包
# def demo(*args, **kwargs):
#
#     print(args)
#     print(kwargs)
#
# #元祖变量/字典变量
# gl_nums = (1, 2, 3)
# gl_dict = {"name": "小明", "age": 18}
# # 拆包语法，简化元祖变量/字典变量的传递
# demo(*gl_nums, **gl_dict)


# 递归
# def sum_numbers(num):
#
#     print(num)
#     # 递归出口，当参数满足某个条件时，不再执行函数
#     if num == 1:
#         return
#     #自己调用自己
#     sum_numbers(num - 1)
#
# sum_numbers(3)


# 递归实现数字累加
# def sum_numbers(num):
#
#     # 出口
#     if num == 1:
#         return 1
#
#     # 假设sum_numbers能够完成num-1的累加
#     temp = sum_numbers(num - 1)
#     # 两个数字相加
#     return temp + num
#
# print(sum_numbers(10))


# 面向对象
# def demo():
#     """测试函数"""
#     print("111")
#
# demo()
# print(demo.__doc__)


# 第一个面向对象程序
# class Cat:
#
#     def eat(self):
#         print("猫爱吃鱼")
#     def drink(self):
#         print("猫要喝水")

# 创建猫对象
# tom = Cat()
# tom.eat()
# tom.drink()
# print(tom)
#
# addr = id(tom)
# print("%x" % addr)
# print(addr)


# 面向对象  小猫实例
# class Cat:
#
#     def eat(self):
#         print("%s爱吃鱼" % self.name)
#     def drink(self):
#         print("%s要喝水" % self.name)
#
# # 创建猫对象
# tom = Cat()
# tom.name = "tom"
# tom.eat()
# tom.drink()
# print(tom)
#
# # 再创建一个猫对象
# lazy_cat = Cat()
# lazy_cat.name = "大懒猫"
# lazy_cat.eat()
# lazy_cat.drink()
# print(lazy_cat)


# 初始化方法
# class Cat:
#
#     def __init__(self):
#
#         print("这是一个初始化方法")
#         self.name = "Tom"
#
#     def eat(self):
#
#         print("%s 爱吃鱼" % self.name)
#
# # 使用类名()创建对象的时候，会自动调用初始化方法__init__
# tom = Cat()
# print(tom.name)
# tom.eat()


# 使用参数设置属性初始值
# class Cat:
#
#     def __init__(self, name):
#
#         print("这是一个初始化方法")
#         self.name = name
#
#     def eat(self):
#
#         print("%s 爱吃鱼" % self.name)
#
# # 使用类名()创建对象的时候，会自动调用初始化方法__init__
# tom = Cat("Tom")
# print(tom.name)
# tom.eat()

# lazy_cat = Cat("Lazy_cat")
# print(lazy_cat.name)
# lazy_cat.eat()


# __del__方法
# class Cat:
#
#     def __init__(self, name):
#         self.name = name
#         print("%s来了!" % self.name)
#
#     def __del__(self):
#         print("%s走了!" % self.name)
#
# # tom是一个全局变量
# tom = Cat("Tom")
# print(tom.name)

# print("-" * 50)



# __str__方法

# class Cat:
#
#     def __init__(self, name):
#         self.name = name
#         print("%s来了!" % self.name)
#
#     def __del__(self):
#         print("%s走了!" % self.name)
#
#     def __str__(self):
#         return "我是小猫%s" % self.name
#
# # tom是一个全局变量
# tom = Cat("Tom")
# print(tom)



# 小明案例
# class Person:
#
#     def __init__(self, name, weight):
#         self.name = name
#         self.weight = weight
#
#     def __str__(self):
#         return "我的名字是%s,体重是%.2f公斤" % (self.name, self.weight)
#
#
#     def run(self):
#         print("%s爱跑步,跑步锻炼身体" % self.name)
#         self.weight -= 0.5
#
#     def eat(self):
#         print("%s是吃货，每次增加1公斤" % self.name)
#         self.weight += 1
#
#
# xiaoming = Person("小明", 75)
# xiaoming.run()
# xiaoming.eat()
# print(xiaoming)
#
# xiaomei = Person("小美", 45)
# xiaomei.run()
# xiaomei.eat()
# print(xiaomei)


# 摆放家具

# 家具类
# class HouseItem:
#
#     def __init__(self, name, area):
#         self.name = name
#         self.area = area
#
#     def __str__(self):
#         return "[%s] 占地 %.2f平方米" % (self.name, self.area)
#
#
# # 房子类
# class House:
#
#     def __init__(self, house_type, area):
#         self.house_type = house_type
#         self.area = area
#
#         # 剩余面积、家具名称列表
#         self.free_area = area
#         self.item_list = []
#
#     def __str__(self):
#         return "户型是 %s\n总面积是 %.2f【剩余面积 %.2f】\n家具 %s" \
#                % (self.house_type, self.area, self.free_area, self.item_list)
#
#     def add_item(self, item):
#         print("要添加 %s" % item)
#         # 1.判断家具面积
#         if item.area > self.free_area:
#             print("%s的面积太大了，无法添加！" % item.name)
#             return
#         # 2.将家具的名称添加到列表中
#         self.item_list.append(item.name)
#         # 3.计算剩余面积
#         self.free_area -= item.area
#
#
# # 1.创建家具对象
# bed = HouseItem("席梦思", 4)
# chest = HouseItem("衣柜", 2)
# table = HouseItem("餐桌", 1.5)
#
# print(bed)
# print(chest)
# print(table)
#
#
# # 2.创建房子对象
# my_home = House("两室一厅", 80)
# my_home.add_item(bed)
# my_home.add_item(chest)
# my_home.add_item(table)
# print(my_home)



# 士兵突击
# class Gun:
#     def __init__(self, model):
#         # 枪的型号
#         self.model = model
#         # 子弹的数量
#         self.bullet_count = 0
#
#     def add_bullet(self, count):
#         self.bullet_count += count
#
#     def shoot(self):
#
#         # 1.判断子弹数量
#         if self.bullet_count <= 0:
#             print("[%s]没有子弹了..." % self.model)
#             return
#
#         # 2.发射子弹
#         self.bullet_count -= 1
#
#         # 3.提示发射信息
#         print("[%s]突突突...[%d]" % (self.model, self.bullet_count))
#
#
# class Soldier:
#     def __init__(self, name):
#         # 1.姓名
#         self.name = name
#         # 2.枪的属性,新兵没有枪
#         self.gun = None
#
#     def fire(self):
#         # 1.士兵有没有枪
#         if self.gun == None:
#             print("[%s]还没有枪" % self.name)
#             return
#         # 2.高喊口号
#         print("冲啊...[%s]" % self.name)
#         # 3.装子弹
#         self.gun.add_bullet(50)
#         # 4.发射子弹
#         self.gun.shoot()
#
#
# # 创建枪对象
# ak47 = Gun("AK47")
#
#
# # 创建许三多
# xusanduo = Soldier("许三多")
# xusanduo.gun = ak47
# xusanduo.fire()
# print(xusanduo.gun)



# 私有属性和私有方法
# class Women:
#
#     def __init__(self, name):
#         self.name = name
#         self.__age = 18
#
#     def __secret(self):
#         # 在对象的方法内部，是可以访问对象的私有属性的
#         print("%s的年龄是%d岁" % (self.name, self.__age))
#
# xiaofang = Women("小芳")
# # 伪私有属性，在外界能够被直接访问
# print(xiaofang._Women__age)
# # 伪私有方法，同样允许在外界直接访问
# xiaofang._Women__secret()



# 单继承

# class Animal:
#
#     def eat(self):
#         print("吃")
#
#     def drink(self):
#         print("喝")
#
#     def run(self):
#         print("跑")
#
#     def sleep(self):
#         print("睡")
#
#
# class Dog(Animal):
#
#     # 子类继承父类的所有的属性和方法
#     def bark(self):
#         print("叫")

# wangcai = Animal()
#
# wangcai.eat()
# wangcai.drink()
# wangcai.run()
# wangcai.sleep()

# wangcai = Dog()

# wangcai.eat()
# wangcai.drink()
# wangcai.run()
# wangcai.sleep()
# wangcai.bark()


# 继承重写
# class Animal:
#
#     def eat(self):
#         print("吃")
#
#     def drink(self):
#         print("喝")
#
#     def run(self):
#         print("跑")
#
#     def sleep(self):
#         print("睡")
#
#
# class Dog(Animal):
#
#     def bark(self):
#         print("叫")
#
#
# class Cat(Animal):
#
#     def catch(self):
#         print("抓老鼠")
#
#
# class XiaoTianQuan(Dog):
#
#     def bark(self):
#         print("汪汪汪...")
#     def fly(self):
#         print("飞")
#
#
# xiaotianquan = XiaoTianQuan()
# xiaotianquan.eat()
# xiaotianquan.drink()
# xiaotianquan.run()
# xiaotianquan.sleep()
# xiaotianquan.bark()
# xiaotianquan.fly()
# print(xiaotianquan)
# tom = Cat()
# tom.catch()


# 扩展父类方法
# class Animal:
#
#     def eat(self):
#         print("吃")
#
#     def drink(self):
#         print("喝")
#
#     def run(self):
#         print("跑")
#
#     def sleep(self):
#         print("睡")
#
#
# class Dog(Animal):
#
#     def bark(self):
#         print("叫")
#
#
# class Cat(Animal):
#
#     def catch(self):
#         print("抓老鼠")
#
#
# class XiaoTianQuan(Dog):
#
#     def fly(self):
#         print("飞")
#
#     def bark(self):
#         # 1.针对子类特有的需求，编写代码
#         print("汪汪汪...")
#         #2.使用super()，调用原本在父类中封装的方法
#         # super().bark()
#         Dog.bark(self)
#         # 3.增加其他子类的代码
#         print("###@@!$#@$@")
#
#
#
# xiaotianquan = XiaoTianQuan()
# xiaotianquan.eat()
# xiaotianquan.drink()
# xiaotianquan.run()
# xiaotianquan.sleep()
# xiaotianquan.bark()
# xiaotianquan.fly()
# print(xiaotianquan)
# tom = Cat()
# tom.catch()


# 私有属性和私有变量
# class A:
#
#     def __init__(self):
#         self.name = 100
#         self.num2 = 200
#
#
# class B(A):
#     pass
#
#
# # 创建一个子类对象
# b = B()
# print(b)



# 父类的私有属性和私有方法
# class Animal:
#
#     def __init__(self):
#         self.num1 = 100
#         self.__num2 = 200
#
#     def __test(self):
#         print("私有方法 %d %d" % (self.num1, self.__num2))
#
#
# class Dog(Animal):
#
#     def demo(self):
#         # 1.在子类的对象方法中不能访问父类的私有属性
#         # print("访问父类的私有属性 %d" % (self.__num2))
#         # 2.在子类的对象方法中不能调用父类的私有方法
#         # self.__test()
#         pass
#
# # 创建一个子类对象
# doggie = Dog()
# print(doggie)
# # 在外界不能直接访问到对象的私有属性或方法
# print(doggie.num1)


# 调用父类的公有方法间接访问私有属性或调用私有方法
# class Animal:
#
#     def __init__(self):
#         self.num1 = 100
#         self.__num2 = 200
#
#     def __test(self):
#         print("私有方法 %d %d" % (self.num1, self.__num2))
#
#     def test(self):
#         print("父类的公有方法 %d" % self.__num2)
#         self.__test()
#
# class Dog(Animal):
#
#     def demo(self):
#         # 1.在子类的对象方法中不能访问父类的私有属性
#         # print("访问父类的私有属性 %d" % self.__num2)
#         # 2.在子类的对象方法中不能调用父类的私有方法
#         # self.__test()
#         pass
#
# # 创建一个子类对象
# doggie = Dog()
# # print(doggie)
# # 在外界访问父类的公有属性或调用公有方法
# doggie.test()
# doggie.num1



# 多继承/多继承注意事项
# class A:
#
#     def test(self):
#         print("A---test方法")
#
#     def demo(self):
#         print("A---demo方法")
#
#
# class B:
#
#     def test(self):
#         print("B---test方法")
#
#     def demo(self):
#         print("B---demo方法")
#
#
# class C(B, A):
#
#     """多继承可以让子类对象，同时具有多个父类的属性和方法"""
#     pass
#
#
# c = C()
# c.test()
# c.demo()


# 多态
# class Dog(object):
#
#     def __init__(self, name):
#         self.name = name
#
#     def play(self):
#         print("%s开心地玩耍..." % self.name)
#
#
# class XiaoTianQuan(Dog):
#
#     def play(self):
#         print("%s在天上玩耍" % self.name)
#
#
# class Person(object):
#
#     def __init__(self, name):
#         self.name = name
#
#     def play_with_dog(self, dog):
#         print("%s 和 %s玩耍" % (self.name, dog.name))
#         dog.play()
#
#
# # 1.创建一个狗对象
# # dog = Dog("小黄")
# xiaotianquan = XiaoTianQuan("哮天犬")
# # 2.创建一个人对象
# mike = Person("麦克")
# # 3.调用人和狗玩耍的方法
# mike.play_with_dog(xiaotianquan)



# 类属性
# class Tool(object):
#
#     # 使用赋值语句，定义类属性，记录创建工具对象的总数
#     count = 0
#
#     def __init__(self, name):
#         self.name = name
#
#         # 针对类属性做一个计数+1
#         Tool.count += 1
#
#
# # 创建工具对象
# tool1 = Tool("斧头")
# tool2 = Tool("镰刀")
# tool3 = Tool("榔头")
# tool4 = Tool("铁锹")
#
# # 输出工具对象的总数
# print(Tool.count)



# 属性获取机制
# class Tool(object):
#
#     count = 0
#
#     def __init__(self, name):
#         self.name = name
#
#         Tool.count += 1
#
#
# tool1 = Tool("斧头")
#
# print(Tool.count)


# 使用对象名访问类属性的问题
# class Tool(object):
#     count = 0
#
#     def __init__(self, name):
#         self.name = name
#
#         Tool.count += 1
#
#
# tool1 = Tool("锄头")
# tool2 = Tool("斧头")
# tool3 = Tool("镰刀")
# # print(Tool.count)
# tool3.count = 99
# print("使用工具是%d" % tool3.count)
# print("==>%d" % Tool.count)



# 类方法
# class Tool(object):
#
#     count = 0
#
#     # 类方法
#     @classmethod
#     def show_tool_count(cls):
#         print("方法个数是%d" % cls.count)
#
#     def __init__(self, name):
#         self.name = name
#         Tool.count += 1
#
#
# tool1 = Tool("斧头")
# tool2 = Tool("镰刀")
# tool3 = Tool("你好")
#
# # 调用类方法
# Tool.show_tool_count()



# 静态方法
# class Dog(object):
#
#     @staticmethod
#     def run():
#         # 不访问实例属性/类属性
#         print("愉快地玩耍")
#
# # 通过类名调用静态方法
# Dog.run()


# 案例演示
# class Game(object):
#
#     def __init__(self, player_name):
#         self.player_name = player_name
#
#     # 历史最高分
#     top_score = 0
#
#     @classmethod
#     def show_top_score(cls):
#         print("最高分是%d" % cls.top_score)
#
#     def start_game(self):
#         print("当前的玩家是%s" % self.player_name)
#         print("游戏开始!")
#
#     @staticmethod
#     def show_help():
#         print("游戏帮助信息")
#
#
# Game.show_help()
# Game.show_top_score()
# player = Game("lisa")
# player.start_game()



# __new__方法
# class MusicPlayer(object):
#
#     def __new__(cls, *args, **kwargs):
#
#         # 1.创建对象时，__new__方法会被自动调用
#         print("创建对象,分配空间")
#         # 2.为对象分配空间
#         instance = super().__new__(cls)
#         # 3.返回对象的引用
#         return instance
#
#     def __init__(self):
#         print("播放器初始化")
#
#
# # 创建播放器对象
# player = MusicPlayer()
# print(player)



# 单例
# class MusicPlayer(object):
#
#     # 记录第一个被创建对象的引用
#     instance = None
#
#     def __new__(cls, *args, **kwargs):
#
#         # 1.判断类属性是否是空对象
#         if cls.instance is None:
#             # 2.调用父类方法，第一个对象分配空间
#             cls.instance = super().__new__(cls)
#
#         # 3.返回类属性保存的对象引用
#         return cls.instance
#
#
# # 创建多个对象
# player1 = MusicPlayer()
# print(player1)
# player2 = MusicPlayer()
# print(player2)



# 单例初始化一次
# class MusicPlayer(object):
#
#     # 记录第一个被创建对象的引用
#     instance = None
#     # 记录是否执行过初始化动作
#     init_flag = False
#
#     def __new__(cls, *args, **kwargs):
#
#         # 1.判断类属性是否是空对象
#         if cls.instance is None:
#             # 2.调用父类方法，第一个对象分配空间
#             cls.instance = super().__new__(cls)
#
#         # 3.返回类属性保存的对象引用
#         return cls.instance
#
#     def __init__(self):
#         # print("初始化播放器")
#         # 1.判断是否执行过初始化动作
#         if MusicPlayer.init_flag:
#             return
#         # 2.如果没有执行过，再执行初始化动作
#         print("初始化播放器")
#         # 3.修改类属性的标记
#         MusicPlayer.init_flag = True
#
#
# # 创建多个对象
# player1 = MusicPlayer()
# print(player1)
# player2 = MusicPlayer()
# print(player2)



# 异常捕获

# try:
#     # 不能确定是否正确的代码
#     num = int(input("请输入一个整数:"))
# except:
#     # 错误的处理代码
#     print("请输入正确的整数")


# 错误类型捕获
# try:
#     num = int(input("请输入一个整数:"))
#     result = 8 / num
#     print(result)
#
# except ValueError:
#     print("请输入正确的整数")
#
# except Exception as result:
#     print("未知错误 %s" % result)


# 异常捕获的完整语法
# try:
#
#     num = int(input("请输入一个整数:"))
#     result = 8/num
#     print(result)
#
# except ValueError:
#
#     print("请输入正确的整数")
#
# except ZeroDivisionError:
#
#     print("除数不能为0")
#
# except Exception as result:
#
#     print("错误类型是%s" % result)
#
# else:
#
#     print(result)
#
# finally:
#
#     print("执行结束")


# 异常传递
# def demo1():
#     return int(input("输入整数:"))
#
# def demo2():
#     return demo1()
#
# try:
#     print(demo2())
# except Exception as result:
#     print("未知错误%s" % result)


# 抛出异常
# def input_password():
#
#     # 1.提示用户输入密码
#     password = input("请输入密码：")
#     # 2.判断密码长度>=8,返回用户输入的密码
#     if len(password) >= 8:
#         return password
#     # 3.如果<8主动抛出异常
#     print("主动抛出异常")
#     # 1.创建异常对象,可以使用错误信息字符串作为参数
#     ex = Exception("密码长度不够")
#     # 2.主动抛出异常
#     raise ex
#
#
# try:
#     print(input_password())
# except Exception as result:
#     print("未知错误是：%s" % result)



# import random
#
# print(random.__file__)
#
# rand = random.randint(1, 10)
# print(rand)
# print(__name__)


# import hm_message
#
# hm_message.send_message.send("你好")
#
# print(hm_message.receive_message.receive())


# 读取文件
# # 1.打开文件
# file = open("README.txt")
# # 2.读取文件
# text = file.read()
# print(text)
# # 3.关闭文件
# file.close()


# 写入文件
# 1.打开文件
file = open("README.txt", "a")
# 2.写入文件
file.write("ya你好")
# 3.关闭文件
file.close()


# 分行读取文件
# file = open("README")
# while True:
#     txt = file.readline()
#     # 判断是否读取到内容
#     if not txt:
#         break
#     print(txt)
#
# file.close()


# 复制小文件   复制大文件
# 打开两个文件
# file1 = open("README")
# file2 = open("HAHAHA", "w")
#
# while True:
#     # 读取一行内容
#     text = file1.readline()
#
#     # 判断是否读取到内容
#     if not text:
#         break
#     file2.write(text)
#
# # 关闭文件
# file1.close()
# file2.close()


# eval函数
# input_str = input("请输入一个算术题:")
# print(eval(input_str))
