# coding:utf-8
import re


def main():

    names = ["name1", "_name__", "2__name", "__name__", "@name", "name!", "name#124"]

    for name in names:
        result = re.match(r"^[a-zA-Z_]+[\w]*$", name)
        if result:
            print("%s符合变量名要求" % name)
        else:
            print("%s非法" % name)


if __name__ == "__main__":
    main()