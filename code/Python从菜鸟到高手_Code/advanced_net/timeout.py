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
http = PoolManager(timeout=Timeout(connect=2,read=2))
url1 = 'https://www.baidu1122.com'
url2 = 'http://httpbin.org/delay/3'
try:
    http.request('GET', url1,timeout=Timeout(connect=2.0,read=4))
except Exception as e:
    print(e)
print('------------')
response = http.request('GET', url2,timeout=Timeout(connect=2,read=4))
print(response.info())
print('------------')
print(response.info()['Content-Length'])
http.request('GET', url2,timeout=Timeout(connect=2,read=2))