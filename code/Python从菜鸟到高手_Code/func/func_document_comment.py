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


def add(x,y):
    "计算两个数的和"
    return x + y
# magic method
print(add.__doc__)
print("----------------")
help(add)
print("----------------")