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

m = re.match('python','I love python.')
if m is not None: 
    print(m.group())
print(m)

m = re.search('python','I love python.')
if m is not None: 
    print(m.group())
print(m)


