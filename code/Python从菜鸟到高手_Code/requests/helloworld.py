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
r = requests.get('https://www.taobao.com')
print(type(r))
print(r.status_code)
print(type(r.text))
print(r.cookies)
print(r.text)

