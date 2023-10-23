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

def sub1(m, n):
    return m - n

print(sub1(20,4))
print(sub1(4,20))

print(sub1(m = 20, n = 4))
print(sub1(n = 4, m = 20))

def sub2(m = 100, n = 50):
    return m - n

    
print(sub2())
print(sub2(45,21))
print(sub2(53, n = 12))
print(sub2(n = 123))
print(sub2(m = 542,n = 143))
print(sub2(53, m = 12))  