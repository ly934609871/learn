# coding:utf-8
import re

# email = input("请输入邮箱:")
# result = re.match(r"^([a-zA-Z0-9_]{4,20})@163.com$", email).group(1)
# print(result)


# html_content = "<h1>hahaha</h1>"
# result = re.match(r"^<(\w*)>.*</\1>$", html_content).group()
# print(result)


html_content = "<body><h1>hahaha</h1></body>"
result = re.match(r"^<(\w*)><(\w*)>.*</\2></\1>$", html_content)
print(result.group(2))