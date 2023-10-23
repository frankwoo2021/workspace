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


dict = {'c':10,'a':40,'b':12,'x':44}
dict['1'] = 3
dict['5'] = 3
print(dict.pop('b'))
for i in range(len(dict)):
    print(dict.popitem())
