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

from urllib3 import *


disable_warnings()
http = PoolManager()

url = 'http://localhost:5000/register'
response = http.request('POST', url,fields={'name':'李宁','age':18})
data = response.data.decode('UTF-8')
print(data)

