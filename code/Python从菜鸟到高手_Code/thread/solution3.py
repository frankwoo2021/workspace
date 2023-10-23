#########################################################################
# 作者:李宁（蒙娜丽宁），UnityMarvel创始人
#
# 微信公众号：极客起源
#
# B站：https://space.bilibili.com/477001733
#
# Copyright © 2022 Lining. All rights reserved.
#
# 版本: 2.0
#########################################################################


from urllib3 import *
import re
import threading
disable_warnings()
http = PoolManager()

f = open('practice/urls.txt', 'r')
urlList = []
while True:
    url = f.readline()
    if url == '':
        break;
    urlList.append(url.strip())
f.close()


class DownloadThread(threading.Thread):
    def __init__(self, func, args):
        super().__init__(target=func,args=args)

def download(filename,url):
    response = http.request('GET', url)
    f = open(filename,'wb')
    f.write(response.data)
    f.close()
    print('<',url,'>','下载完成')
for i in range(len(urlList)):
    thread = DownloadThread(download,(str(i) + '.jpg',urlList[i]))
    thread.start()