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

while True:
    x = input("请输入一个数：")
    if x == "end":
        break;
    num = int(x)
    if num % 2 == 0:
        print(x + "是偶数") 
    else:
        print(x + "是奇数")