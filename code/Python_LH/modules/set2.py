#########################################################################
# 作者:李宁（蒙娜丽宁）
#
# 微信公众号：极客起源
#
# B站：https://space.bilibili.com/477001733
#
# Copyright © 2022 Lining. All rights reserved.
#
# 版本: 2.0
#########################################################################

a = set([1,2])
b = set([10,20])

a.add(4)
print(a)
# a.add(b)
a.add(frozenset(b))
print(a)
d = {'Bill':30,'Mike':40}
#d[a] = 60
d[frozenset(a)] = 60

print(d)
t = [1,2,3]
tt = (1,2,3)
# d[t] = 111
#a.add(t)
#a.add(d)
a.add(tt)
print(a)



