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

name = "Bill"							#  定义变量name
assert name == "Bill"					#  断言条件表达式的值是True，继续执行下面的语句

age = 20								#  定义变量age
#  断言条件表达式的值是False，抛出异常，后面的代码不会被执行
assert 0 < age < 10, "年龄必须小于10岁"

print("hello world")		# 这行代码不会被执行
