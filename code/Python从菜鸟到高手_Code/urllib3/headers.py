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

from urllib3 import *
disable_warnings()
http = PoolManager()
url = 'https://www.baidu.com'
response = http.request('GET', url)
# 输出HTTP响应头信息（以字典形式返回HTTP响应头信息）
for key in response.info().keys():
    print(key,':', response.info()[key])


