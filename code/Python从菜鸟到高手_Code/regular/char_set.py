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
m = re.match('[ab][cd][ef][gh]', 'adfh')
print(m.group())

m = re.match('[ab][cd][ef][gh]', 'bceg')
print(m.group())

m = re.match('[ab][cd][ef][gh]', 'abceh')  # 不匹配
print(m)

m = re.match('ab[cd][ef][gh]', 'abceh')  # 匹配
print(m.group())
print(m)

m = re.match('abcd|efgh', 'efgh')  # 匹配
print(m.group())
print(m)


