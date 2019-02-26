# coding:utf-8


# search 查找
# import re
#
# result = re.search(r"\d+", "阅读量是9999").group()
# print(result)


# findall  返回值是列表  不需要用到group
# import re
#
# result = re.findall(r"\d+", "阅读量为999，点赞数为99，评论量为9")
# print(result)


# sub 对匹配到的数据进行替换
# import re
#
# result = re.sub(r"\d+", "99", "阅读量为9999")
# print(result)


# sub案例
# import re
#
#
# def add(temp):
#
#     strNum = temp.group()
#     num = int(strNum) + 1
#     return str(num)
#
#
# result = re.sub(r"\d+", add, "阅读量为998")
# print(result)


# split  字符串切割，返回列表
# import re
#
# result = re.split(r":| ", "info:xiaozhang 33 hubei")
# print(result)


import re

html_content = """<dd class="job_bt">
        <h3 class="description">职位描述：</h3>
        <div>
        <p>1、参与电商平台系统搭建，并完成数据模型建立；<br>2、设计爬虫策略和反屏蔽规则，解决封账号、封IP、验证码等难点攻克。</p>
<p>3、负责企业信息系统及数据库的设计与开发；</p>
<p>4、负责企业自动化系统开发及测试（重点）；</p>
<p>5、负责数据部门的业务处理自动化及相关工作。<br><br>任职资格：<br>1、熟练使用python语言，二年以上开发工作经验；<br>2、 熟悉linux系统，熟练使用bash编程优先；<br>3、了解数据库基本原理，熟练使用mysql优先；<br>4、了解基本的计算机网络、数据结构和算法；<br>5、有大数据处理分析、自动化系统开发经验的优先；<br>6、具备基本的团队协作能力，能够跟团队共进退，互相帮助</p>
        </div>
    </dd>"""

# result1 = re.sub(r"<.*?>", "", html_content)
# result = re.sub(r" |\n", "", result1)
# print(result)


result = re.sub(r"<.*?>| |\n", "", html_content)
print(result)