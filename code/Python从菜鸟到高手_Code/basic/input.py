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

name = input("请输入你的名字：")				# 输入姓名，并把输入的结果赋给name变量
age = int(input("请输入你的年龄："))			# 输入年龄，并把输入的结果赋给age变量
salary = float(input("请输入你的收入："))		# 输入收入，并把输入的结果赋给salary变量

print("姓名：", name)						# 输出姓名
print("年龄：", age)						# 输出年龄
print("收入：", format(salary, "0.1f"))		# 输出收入
