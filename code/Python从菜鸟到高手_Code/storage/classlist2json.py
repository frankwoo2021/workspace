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

f = open('files/products.json','r', encoding='utf-8')
jsonStr = f.read()

products = json.loads(jsonStr, object_hook=Product)
print(type(products))
for product in products:     
    print('name', '=', product.name)
    print('price', '=', product.price)
    print('count', '=', product.count)   
f.close()

def product2Dict(product):   
    return {
        'name': product.name,
        'price': product.price,
        'count': product.count
        }

jsonStr = json.dumps(products, default=product2Dict,ensure_ascii=False)
print(jsonStr)
