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
http = PoolManager(cert_reqs='CERT_NONE')
url = 'https://www.baidu.com'
#url = 'http://httpbin.org/delay/3'
response = http.request('GET', url,timeout=Timeout(connect=2,read=4))
print(response.info())
print('------------')
print(response.info()['Content-Length'])
