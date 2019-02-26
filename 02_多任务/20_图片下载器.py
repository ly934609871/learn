# coding:utf-8
import urllib.request
import gevent
from gevent import monkey

monkey.patch_all()


def downloader(img_name, img_url):
    request = urllib.request.urlopen(img_url)

    # 读取请求内容
    img_content = request.read()

    #
    with open(img_name, "wb") as f:
        f.write(img_content)


def main():
    gevent.joinall([
        gevent.spawn(downloader, "1.png", "http://live-cover.msstatic.com/huyalive/90931-2694434440-115725078010160742"
                                          "40-""2980461690-10057-A-0-1/20181214132723.jpg?x-oss-process=image/resize,l"
                                          "imit_0,m_""fill,w_338,h_190/sharpen,80/format,jpg/interlace,1/quality,q_90"),
        gevent.spawn(downloader, "2.png", "http://live-cover.msstatic.com/huyalive/99173389-99173389-42594646238848614"
                                          "4-""2708445338-10057-A-0-1/20181214133747.jpg?x-oss-process=image/resize,l"
                                          "imit_0,m_""fill,w_338,h_190/sharpen,80/format,jpg/interlace,1/quality,q_90"),
        gevent.spawn(downloader, "3.png", "https://rpic.douyucdn.cn/asrpic/181214/2004384_1344_0.jpg/dy1")

    ])


if __name__ == "__main__":
    main()

