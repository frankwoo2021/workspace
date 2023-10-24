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

print(1,end=" ")
print(2,end=" ")
print(3,end=" ")
print(4,end=" ")
print(5,end=" ")
print(6,end=" ")
print(7,end=" ")
print(8,end=" ")
print(9,end=" ")
print(10)

# 用while循环输出1到10
print("用while循环输出1到10")
x = 1
while x <= 10:
    print(x,end=" ")
    x += 1

#  定义一个列表
numbers = [1,2,3,4,5,6,7,8,9,10]
print("\n用for循环输出列表中的值（1到10）")
for num in numbers:
    print(num, end= " ")
# 用range函数生成一个元素值从1到9999的列表
numbers = range(1,10000)
print("\n用for循环输出列表中的值（1到9999）")
for num in numbers:
    print(num, end= " ")
print("\n用for循环输出列表中的值的乘积（1到99）")
# 用range函数生成一个元素值为0到99的的列表，并对该列表进行迭代
for num in range(100):			# range函数如果只指定一个参数，产生的列表元素值从0开始
    print(num * num, end= " ")
