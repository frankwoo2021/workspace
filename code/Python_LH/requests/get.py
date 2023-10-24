#########################################################################
# 作者:李宁（蒙娜丽宁）
#
# 微信公众号：极客起源
#
# B站：https://space.bilibili.com/477001733
#
# Copyright © 2022 Lining. All rights reserved.
#
# 版本: 2.0
#########################################################################

import requests
data = {
    'name':'Bill',
    'country':'中国',
    'age':20
}

r = requests.get('http://httpbin.org/get?name=Mike&country=美国&age=40',params=data)
print(r.text)
print(r.json())
print(r.json()['args']['country'])
