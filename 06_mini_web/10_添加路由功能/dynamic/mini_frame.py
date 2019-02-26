# coding:utf-8
from pymysql import *
import re

URL_FUNC_DICT = dict()


def route(url):
    # 装饰器中的参数传递给了url
    def set_func(func):
        # 装饰器中的函数名传递给了func
        # URL_FUNC_DICT["/index.py"] = index
        URL_FUNC_DICT[url] = func
        def call_func(*args, **kwargs):
            return func(*args, **kwargs)
        return call_func
    return set_func


@route("/index.html")
def index():
    with open("./templates/index.html") as f:
        content = f.read()

        # 创建Connection连接
        conn = connect(host='localhost', port=3306, user='root', password='ly031012',
                       database='stock_db', charset='utf8')
        # 获得Cursor对象
        cursor = conn.cursor()
        cursor.execute("select * from info;")
        stock_infos = cursor.fetchall()
        cursor.close()
        conn.close()

        tr_template = """<tr>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>
            <input type="button" value="添加" id="toAdd" name="toAdd" systemidvalue="000007">
            </td>
            </tr>
        """
        html = ""
        for line_info in stock_infos:
            html += tr_template % (line_info[0], line_info[1], line_info[2], line_info[3], line_info[4],
                                   line_info[5], line_info[6], line_info[7])

        content = re.sub(r"\{%content%\}", html, content)

    return content


@route("/center.html")
def center():
    with open("./templates/center.html") as f:
        content = f.read()

        # 创建Connection连接
        conn = connect(host='localhost', port=3306, user='root', password='ly031012',
                       database='stock_db', charset='utf8')
        # 获得Cursor对象
        cursor = conn.cursor()
        cursor.execute("select i.code, i.short, i.chg, i.turnover, i.price, i.highs, f.note_info from info as i "
                       "inner join focus as f on i.id = f.info_id")
        stock_infos = cursor.fetchall()
        cursor.close()
        conn.close()

        tr_template = """
            <tr>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>
                    <a type="button" class="btn btn-default btn-xs" href="/update/300268.html"> 
                    <span class="glyphicon glyphion-star" aria-hidden="true"></span> 修改 </a>
                </td>
                <td>
                    <input type="button" value="删除" id="toDel" name="toDel" systemidvalue="300268">
                </td>
            </tr>
        """
        html = ""
        for line_info in stock_infos:
            html += tr_template % (line_info[0], line_info[1], line_info[2], line_info[3], line_info[4],
                                   line_info[5], line_info[6])

        content = re.sub(r"\{%content%\}", html, content)
    return content


def application(environ, start_response):
    start_response("200 OK", [("Content-Type", "text/html;charset=utf-8")])
    file_name = environ["PATH_INFO"]
    # if file_name == "/index.html":
    #     return index()
    # elif file_name == "/center.html":
    #     return center()
    # else:
    #     return "hello python  你好啊小老弟"
    try:
        # func = URL_FUNC_DICT[file_name]
        # return func()
        return URL_FUNC_DICT[file_name]()
    except Exception as ret:
        return ("异常类型是%s" % str(ret))


