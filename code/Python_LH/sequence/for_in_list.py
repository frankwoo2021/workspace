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

a_tuple = ('李宁', '蒙娜丽宁', '极客起源')
for value in a_tuple:
    print('当前元素是:', value)
print('-------------')
new_list = [15, 44, 3.2, 64, True, 'hello world', 56, '极客起源', 6666]
my_sum = 0
my_count = 0
for value in new_list:
    # 如果该元素是整数或浮点数
    if isinstance(value, int) or isinstance(value, float):
        print(value)
        # 累加该元素
        my_sum += value
        # 数值元素的个数加1
        my_count += 1
print('总和:', my_sum)
print('平均数:', my_sum / my_count)