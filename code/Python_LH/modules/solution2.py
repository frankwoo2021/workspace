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

from datetime import *

while True:
    try:
        d1 = input('请输入第1个日期：');
        d1 = datetime.strptime(d1, '%Y-%m-%d')
        d2 = input('请输入第2个日期：');
        d2 = datetime.strptime(d2, '%Y-%m-%d')
        d = d2 - d1
        print('两个日期之间相距%d天' % d.days)
    except Exception as e:
        print(e)


