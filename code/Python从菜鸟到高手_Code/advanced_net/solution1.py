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
import re
disable_warnings()
http = PoolManager()

url = 'https://www.taobao.com/'
def str2Headers(file):
    headerDict = {}
    f = open(file,'r')
    headersText = f.read()
    headers = re.split('\n',headersText)
    for header in headers:
        result = re.split(':',header,maxsplit = 1)
        headerDict[result[0]] = result[1]
    f.close()
    return headerDict
headers = str2Headers('headers.txt')
response = http.request('GET', url,headers=headers)
result = re.search('charset=([^\)\']*)',response.info()['Content-Type'])
charset = result.group(1)

data = response.data.decode(charset)
print(data)

