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

numbers = 1,2,3     				# 创建元组
print(numbers)						# 运行结果：(1, 2, 3)

names = ("Bill", "Mike", "Jack")
print(names)						# 运行结果：('Bill', 'Mike', 'Jack')


values = 40,						# 创建一个值的元组
print(values)						# 运行结果：(40,)

# 生成5个同样值的元组
print(5 * (12 + 4,))				#  运行结果：(16, 16, 16, 16, 16)
# 不是元组，就是一个数
print(5 * (12 + 4))				#  运行结果：80

# 将一个序列转换为元组（tuple函数）
print(tuple([1,2,3]))				#  运行结果：(1, 2, 3)
print(tuple("geekori"))				#  运行结果：('g', 'e', 'e', 'k', 'o', 'r', 'i')
