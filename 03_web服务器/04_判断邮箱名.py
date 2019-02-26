# coding:utf-8
import re


def main():
    email_list = ["xiaoWang@163.com", "xiaoWang@163.comheihei", ".com.xiaowang@qq.com"]
    for email in email_list:
        # \用于转义
        result = re.match(r"^[a-zA-Z0-9_]{4,20}@163\.com$", email)
        if result:
            print("邮箱%s符合要求" % email)
        else:
            print("邮箱%s不符合要求" % email)


if __name__ == "__main__":
    main()