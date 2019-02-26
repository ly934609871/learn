import re

# result = re.match(r"hello", "hello world")
# print(result)

# result = re.match(r"速度与激情\d", "速度与激情1")
# print(result.group())

# [12345678]、[1-8]表示只能匹配1-8
# result = re.match(r"速度与激情[12345678]", "速度与激情1")
# print(result.group())

# result = re.match(r"速度与激情\w", "速度与激情k")
# print(result.group())

import re

content = "mini_frame:application"
result = re.match(r"([^:]+):(.*)", content).group(2)
print(result)