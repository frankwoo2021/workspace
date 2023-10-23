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

import datetime
d1 = datetime.datetime(2017, 4, 12)
d2 = datetime.datetime(2018, 12, 25)
print((d2 - d1).days)

d1 = datetime.datetime(2017, 4, 12,10,10,10)
d2 = datetime.datetime(2018, 12, 25,10,10,40)
print(d2 - d1)
print((d2 - d1).seconds)

d1 = datetime.datetime.now()

d2 = d1 + datetime.timedelta(hours=10)
import time
d2 = time.localtime(d2.timestamp())
print (time.strftime("%Y-%m-%d %H:%M:%S", d2))

