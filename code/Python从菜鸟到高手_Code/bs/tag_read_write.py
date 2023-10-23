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

# 读取和设置节点的属性
html = '''
<html>
    <head><title>index</title></head>
    <body attr='test xyz' class='style1 style2'>
        <a rel='ok1 ok2 ok3' class='a1 a2' href='a.html'>first page</a>
        <p>
        <a href='b.html'>second page</a>
        <p>
        <a  href='c.html'>third page</a>
        <p>
        <x k='123' attr1='hello' attr2='world'>hello</x>
    </body>
</html>
'''
from bs4 import *

soup = BeautifulSoup(html,'lxml')
print(type(soup.body.attrs))
print('body.class','=',soup.body['class'])
print('body.attr','=',soup.body['attr'])
print('a.class','=',soup.a['class'])
soup.x['attr1'] = 'ok'
print('x.attr1','=',soup.x['attr1'])

soup.body['class'] = ['x','y','z']
soup.body['class'].append('ok')
print(soup.body)
print(soup.a['rel'])
# class、rel,rev,accept-charset,headers,accesskey

