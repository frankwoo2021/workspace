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

floorStr = input("请输入星号塔的层数：")

floor = int(floorStr) 
num = floor * 2 - 3
while floor > 0:
    print("{:<{a}}{:*<{b}}".format(" ","",a=floor,b=(num - (floor - 2)*2 )))
    floor -= 1

'''
print("{:<10}{:*<1}".format(" ",""))
print("{:<9}{:*<3}".format(" ",""))
print("{:<8}{:*<5}".format(" ",""))

print("{:<7}{:*<7}".format(" ",""))

print("{:<6}{:*<9}".format(" ",""))

print("{:<5}{:*<11}".format(" ",""))

print("{:<4}{:*<13}".format(" ",""))

print("{:<3}{:*<15}".format(" ",""))

print("{:<2}{:*<17}".format(" ",""))
print("{:<1}{:*<19}".format(" ",""))
'''