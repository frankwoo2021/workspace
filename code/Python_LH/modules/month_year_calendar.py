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

import calendar
import locale

cal = calendar.month(2017, 1)

print(cal);

locale.setlocale(locale.LC_ALL, 'zh_CN.UTF-8')

cal = calendar.month(2017, 1)

print(cal);
locale.setlocale(locale.LC_ALL, '')
print(calendar.calendar(2017))

