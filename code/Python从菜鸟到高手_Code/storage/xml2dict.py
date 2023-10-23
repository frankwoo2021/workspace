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
# pip3 install xmltodict
import xmltodict
f = open('files/products.xml','rt',encoding="utf-8")
xml = f.read()
import pprint
d = xmltodict.parse(xml)
print(d)
print(type(d))
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(d)
f.close()

