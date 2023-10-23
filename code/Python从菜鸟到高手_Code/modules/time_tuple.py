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

import time

localtime = time.localtime(time.time())
print ("本地时间为 :", localtime)
print('年','=', localtime.tm_year)
print('月','=', localtime.tm_mon)
print('日','=', localtime.tm_mday)
print('一年的第%d' % localtime[7])
localtime = time.asctime( time.localtime(time.time()) )
print ("本地时间为 :", localtime)

