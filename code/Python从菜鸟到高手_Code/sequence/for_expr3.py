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

num_list = [2 * [x, y] for x in range(5) for y in range(4)]
'''
num_list = []
for x in range(5):
    for y in range(4):
        num_list.add(2 * [x,y])
'''
# num_list列表包含20个元素
print(num_list)
last_list = []
for x in range(5):
    for y in range(4):
        last_list.append(2 * [x, y])
print(last_list)

num_list = [[x, y, z] for x in range(5) for y in range(4) for z in range(8)]
# 3_list列表包含160个元素
print(num_list)

num_list1 = [30, 12, 77, 34, 39, 78, 36, 36, 121]
num_list2 = [3, 6, 7, 12]
# 只要y能整除x，就将它们配对在一起
result = [(x, y) for x in num_list2 for y in num_list1 if y % x == 0]
print(result)
