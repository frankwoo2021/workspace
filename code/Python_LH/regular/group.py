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
m = re.match('(\d{3})-(\d{4})-([a-z]{2})', '123-4567-xy')

if m is not None:
    print(m.group())
    print(m.group(1))
    print(m.group(2))
    print(m.group(3))
    print(m.groups())
print('-----------------')
m = re.match('(\d{3}-\d{4})-([a-z]{2})', '123-4567-xy')
if m is not None:
    print(m.group())
    print(m.group(1))
    print(m.group(2))
    print(m.groups())
print('-----------------')
m = re.match('\d{3}-\d{4}-([a-z]{2})', '123-4567-xy')
if m is not None:
    print(m.group())
    print(m.group(1))
    print(m.groups())
print('-----------------')
m = re.match('\d{3}-\d{4}-[a-z]{2}', '123-4567-xy')
if m is not None:
    print(m.group())
    print(m.groups())