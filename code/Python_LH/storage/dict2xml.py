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
# pip3 install dicttoxml
import dicttoxml
import collections
import os
from xml.dom.minidom import parseString

d = [20,'names',
     {'name':'Bill','age':30,'salary':2000},
     {'name':'王军','age':34,'salary':3000},
     {'name':'John','age':25,'salary':2500}]
collections.Iterable = collections.abc.Iterable
bxml = dicttoxml.dicttoxml(d, custom_root = 'persons')

xml = bxml.decode('utf-8')
print(xml)

dom = parseString(xml)

prettyxml = dom.toprettyxml(indent = '  ')
print(prettyxml)
os.makedirs('files', exist_ok = True)
f = open('files/persons.xml', 'w',encoding='utf-8')
f.write(prettyxml)
f.close()