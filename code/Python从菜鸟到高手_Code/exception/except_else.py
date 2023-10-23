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
    try:
        x = int(input('请输入分子：'))
        y = int(input('请输入分母：'))
        value = x / y
        print('x / y is', value)         
    except Exception as e:
        print('不正确的输入：',e)
        print('请重新输入')
    else:
        print('else')
        break