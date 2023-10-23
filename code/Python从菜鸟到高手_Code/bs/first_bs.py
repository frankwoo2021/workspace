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

# Beautiful Soup基础：使用Beautiful Soup
from bs4 import BeautifulSoup

soup1 = BeautifulSoup('<title>html.parser测试</title>','html.parser')
print(soup1.title)
print(soup1.title.text)
print('-----------')
soup2 = BeautifulSoup('<title>lxml测试</title>','lxml')
print(soup2.title.text)
print('-----------')
html = '''
<html>
    <head><title>html5lib测试</title></head>
    <body>
        <a href='a.html'>first page</a>
        <p>
        <a href='b.html'>second page</a>
        <p>
        <a href='c.html'>third page</a>
        <p>
    </body>
</html>
'''
soup3 = BeautifulSoup(html,'html5lib')
print(soup3.title)
print(soup3.title.text)
print(soup3.a['href'])