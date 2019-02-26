# coding:utf-8

import re

#  \d{1, 2} 表示可以匹配1位或者2位的数字   \d{1,3}表示可以匹配1位、2位或3位的数字
# result = re.match(r"人不彪悍枉少年\d{1,2}", "人不彪悍枉少年16")
# print(result.group())


# \d{11}表示只能匹配11位数字  限制位数
# result = re.match(r"\d{11}", "12345543211")
# print(result.group())


# 匹配电话号码   -？表示要么有一个-，要么没有-
# result = re.match(r"\d{3}-?\d{8}", "010-11111111")
# print(result.group())


content = """hahah
asdf
wwww
ertyu
qdadac
"""

# .*表示要么有，要么有多个，要么没有
# re.S匹配换行符
# .+表示最少匹配一个字符，不能匹配空字符
result = re.match(r".*", content, re.S)
print(result.group())