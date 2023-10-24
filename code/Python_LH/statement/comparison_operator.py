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

'''
==
<
>
<=
>=
!=
x is y：x和y是同一个对象
x is not y：x和y是不同的对象
x in y：x是y容器的成员
x not in y：x不是y容器的成员
'''
print(20 == 30)			#  判断20和30是否相等，运行结果：False
x = 20
y = 40
print(x < y)				#  判断x是否小于y，运行结果：True
if x > y:					#  条件不满足
    print("x > y")
else:						#  条件满足
    print("x <= y")
s1 = "hello"
s2 = "Hello"
if s1 >= s2 and x > y:		# 条件不满足
    print("满足条件")
elif not s1 < s2:			# 条件满足
    print("基本满足条件")
else:						# 条件不满足
    print("不满足条件")
