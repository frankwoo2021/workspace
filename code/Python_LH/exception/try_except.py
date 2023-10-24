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

x = None

while True:
    try:
        if x == None:
            x = int(input("请输入分子："))
        y = int(input("请输入分母："))
        print("x / y = {}".format(x / y))
        break;
    except :
        print("分母不能为0，请重新输入分母！")


