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

url = input("请输入一个Https网址：")
scheme = url[0:5]					#  分片获取Url中的Scheme
host = url[8:]						#  分片获取Url中的Host

print("scheme:", scheme)
print("host:",host)

str = input("请输入一个整数:")
n = int(str);

numbers = range(1,n)				# 产生包含1到n的数值类型的序列
numbers1 = numbers[0::2]			# 分片获取序列中的奇数
numbers2 = numbers[1::2]			# 分片获取序列中的偶数
for number in numbers1:				# 在第1行输出所有的奇数
    print(number, end= " ")
print("")
print(" ",end="")
for number in numbers2:				# 在第2行错位输出所有的偶数
    print(number, end= " ")
