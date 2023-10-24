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

import fileinput
fileobj = fileinput.input('./files/urls.txt')

print(type(fileobj))
print(fileobj.readline().rstrip())
for line in fileobj:    
    line = line.rstrip()
    if line != '':
        print(fileobj.lineno(),':',line)
    else:
        print(fileobj.filename())  # 必须在第1行读取后再调用，否则返回None