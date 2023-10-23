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

from xml.etree.ElementTree import parse

doc = parse('files/products.xml')

for item in doc.iterfind('products/product'):
    id = item.findtext('id')
    name = item.findtext('name')
    price = item.findtext('price')
    print('uuid','=',item.get('uuid'))
    print('id','=',id)
    print('name', '=',name)
    print('price','=',price)
    print('-------------')
