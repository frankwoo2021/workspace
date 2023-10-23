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

num_range = range(10) # 0 到 9
# 对num_range执行for表达式
num_list1 = (x + x for x in num_range)
'''
num_list1 = []
for x in num_range:
    num_list1.add(x + x)

'''
print(type(num_list1))
num_list2 = [x + x for x in num_range]
print(type(num_list2))

for num in num_list1:
    print(num, end=' ')
print()
# num_range集合包含10个元素
print(num_list2)




