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

def add1(x,y,z):
    return x + y + z
print(add1(1,2,3))

list = [2,3,4]   # 可以用列表或元组
print(add1(*list))

dict = {'x':100, 'y':200, 'z':12}
print(add1(**dict))

def add2(*numbers):
    result = 0
    for number in numbers:
        result += number
    return result
print(add2(1,2,3,4,5,6,7,8,9))
print(add2(*list))

def add3(**numbers):
    result = 0
    for item in numbers.items():
       result += item[1] 
    return result

print(add3(**dict))

def add4(numbers):
    result = 0
    for item in numbers.items():
       result += item[1] 
    return result

print(add4(dict))

