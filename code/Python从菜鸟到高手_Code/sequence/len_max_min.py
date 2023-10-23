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

values = [10,40,5,76,33,2,-12]
print(len(values))					# 运行结果：7
print(max(values))					# 运行结果：76
print(min(values))					# 运行结果：-12
print(max(4,3,2,5))				# 运行结果：5
print(min(6,5,4))					# 运行结果：4
print(max("abc",5,4))			     # 字符串和数字不能比较，将抛出异常
list = ["x",5,4]
print(min(list))			          # 字符串和数字不能比较，将抛出异常
