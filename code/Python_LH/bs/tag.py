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

from bs4 import BeautifulSoup
html = '''
<html>
    <head><title>index</title></head>
    <body>
        <a href='a.html'>first page</a>
        <p>
        <a href='b.html'>second page</a>
        <p>
        <a href='c.html'>third page</a>
        <p>
        <x k='123'>hello</x>
    </body>
</html>
'''
soup = BeautifulSoup(html,'lxml')
print(soup.a)
print(soup.body.a)
print(soup.a.string)
# ----设置节点名称------
soup.a.name = 'div'
print(soup.x)
print('--------')
print(soup.x.string)

soup.x.string = 'word'
print(soup.x)
