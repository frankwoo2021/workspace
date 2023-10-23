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

import re
s1 = '^[bh][aiu]t$'
list = ['bat','Bit','But','hAt','hit','hut']
for value in list:
    print(re.match(s1, value,re.I))
    