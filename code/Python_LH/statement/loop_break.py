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

x = 0
while x < 100:								# 开始while循环
    if x == 5:								# 当x == 5时终止循环
        break;
    print(x, end=" ")
    x += 1
names = ["Bill", "Mike", "Mary"]			# 定义一个列表变量
print("\nbreak语句在for循环中的应用")
for name in names:							# 对names列表进行迭代
    if not name.startswith("B"):				# 遇到列表元素值不是以B开头的，就终止for循环
        break;
    print(name)

print("break语句在for循环中的应用")
for name in names:							#  对names列表进行迭代
    #  遇到列表元素值以B开头的，会跳过本次循环，继续执行下一次循环
    if name.startswith("B"):
        continue;
    print(name, end=" ")

print("\n嵌套循环")
arr1 = [1,2,3,4,5]
arr2 = ["Bill", "Mary", "John"]
arr = [arr1, arr2]							#  定义一个二维列表变量
i = 0;
while i < len(arr):						#  使用嵌套循环枚举二维列表中的每一个元素值
    for value in arr[i]:
        print(value, end = " ")			#  输出二维列表中的元素值
    i += 1
    print()
