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

import random
x = 0
while x < 10:
    x += 1
    if x == random.randint(1, 20):
        print(x)
        break;
else:  # while循环的else子句
    print("没有中断while循环")

numbers = [1, 2, 3, 4, 5, 6]
for number in numbers:
    if number == random.randint(1, 12):
        print(number)
        break;
else:  # for循环的else子句
    print("正常退出循环")
