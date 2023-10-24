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
s = 'Bill|Mike|John'
m = re.match(s, 'Bill')
if m is not None:
    print(m.group())
m = re.match(s, "Bill:my friend")
if m is not None:
    print(m.group())

m = re.search(s,'Where is Mike?')
if m is not None:
    print(m.group())
print(m)
