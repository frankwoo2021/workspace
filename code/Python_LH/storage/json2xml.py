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
import dicttoxml
import collections
collections.Iterable = collections.abc.Iterable
f = open('files/products.json','r',encoding='utf-8')
jsonStr = f.read()
d = json.loads(jsonStr)
print(d)
xmlStr = dicttoxml.dicttoxml(d).decode('utf-8')
print(xmlStr)
f.close()
