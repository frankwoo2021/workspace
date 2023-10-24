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
url = 'http://localhost:5000'
while True:
    filename = input('请输入要上传的文件名字（必须在当前目录下）：')
    if not filename:
        break
    with open(filename,'rb') as fp:
        fileData = fp.read()
    response = http.request('POST',url,fields={'file':(filename,fileData)})
    print(response.data.decode('utf-8'))
