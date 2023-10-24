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

s = "I not only like python, but also like kotlin."
table = s.maketrans("ak", "*$")
print(table)
print(len(table))

print(s.translate(table))

table1 = s.maketrans("ak", "$%", " ")
print(s.translate(table1))
