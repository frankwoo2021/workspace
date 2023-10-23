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
m = re.search('^The', 'The end.')
print(m)
if m is not None:
    print(m.group())
m = re.search('^The', 'end. The')
print(m)
if m is not None:
    print(m.group())

m = re.search('The$', 'end. The')
print(m)
if m is not None:
    print(m.group())
m = re.search('The$', 'The end.')
print(m)
if m is not None:
    print(m.group())
    
m = re.search(r'\bthis', "What's this?")
print(m)
if m is not None:
    print(m.group())
m = re.search(r'\bthis', "What'sthis?")
print(m)
if m is not None:
    print(m.group())

m = re.search(r'\bthis\b', "What's this?")
print(m)
if m is not None:
    print(m.group())
m = re.search(r'\bthis\b', "What's thisa")
print(m)
if m is not None:
    print(m.group())