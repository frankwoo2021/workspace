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

from socket import *
import re
from time import ctime
import os
def responseHeaders(file,length):
    f = open(file,'r')
    
    headersText = f.read()
    headersText = headersText % length
    return headersText


def filePath(get):
    if get == '/':
        return 'static' + os.sep + 'index.html'
    else:
        paths = get.split('/')
        s = 'static'
        for path in paths:
            if path.strip() != '':
                s = s + os.sep + path 
        return s
    
print(os.path.exists('a'))
        