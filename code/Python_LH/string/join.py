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

list = ['a','b','c','d','e']
s = "+"
print(s.join(list))

dirs = '','usr','local','nginx',''
linuxPath = '/'.join(dirs)
windowPath = 'C:' + '\\'.join(dirs)
print(linuxPath)
print(windowPath)

numList = [1,2,3,4,5]
print(s.join(numList)) 
