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
m = re.match('hello', 'hello')
if m is not None:
    print(m.group())
print(m.__class__.__name__)

m = re.match('hello', 'world')
if m is not None:
    print(m.group())
print(m)
# 只要模式从字符串起始位置开始，也可以匹配成功
m = re.match('hello', 'hello world')
if m is not None:
    print(m.group())
print(m)