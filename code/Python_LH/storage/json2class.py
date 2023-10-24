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

import json
class Product:
    def __init__(self, d):
        self.__dict__ = d

f = open('files/product.json','r')
jsonStr = f.read()
#  JSON字符串转换为类实例
my1 = json.loads(jsonStr, object_hook=Product)
print('name', '=', my1.name)
print('price', '=', my1.price)
print('count', '=', my1.count)
print('-----------')
def json2Product(d):
    return Product(d)
my2 = json.loads(jsonStr, object_hook=json2Product)
print('name', '=', my2.name)
print('price', '=', my2.price)
print('count', '=', my2.count)
f.close()
