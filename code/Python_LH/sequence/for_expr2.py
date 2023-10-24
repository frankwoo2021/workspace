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

num_range = range(10)
num_list = [x + x for x in num_range if x % 2 == 1]
'''
num_list = []
for x in num_range:
    if x % 2 == 1:
        num_list.add(x + x)

'''
# a_list集合包含10个元素
print(num_list)

