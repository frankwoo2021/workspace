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
from bs4 import BeautifulSoup
disable_warnings()

html = '''
<html>
    <head><title>我的网页</title></head>
    <body attr="test" class = "style1">
    <a href='aa.html'>aa.html</a>
    <a href='bb.html' class = "style1">bb.html</a>
    <b>xyz</b>
    </body>
</html>
'''
soup = BeautifulSoup(html,"lxml")
from bs4 import NavigableString
def filterFun(tag):
    if tag.has_attr('class'):
        if 'style1' in tag['class']:
            return True
    return False

for tag in soup.find_all(filterFun):
    print(tag)
    print('------------')
