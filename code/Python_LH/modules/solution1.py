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


import random
import os

strList = ['abc','bbb',30,'xyz','ddd','ok','666']
dirs = random.sample(strList, 3)
print(dirs)
dirStr = ''
for dir in dirs:
    dir += os.sep
    dirStr += dir 
print(dirStr)
os.makedirs(dirStr, exist_ok=True)

