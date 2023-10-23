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

numbers = []
while True:
    numStr = input("请输入一个整数：")
    if numStr == "end":
        break;
    num = int(numStr)
    numbers.append(num)
    
numbers.sort(reverse = True)

print(numbers)