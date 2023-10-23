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

# 序列封包：将10、20、30封装成元组后赋值给vals
values = 10, 20, 30
print(values) # (10, 20, 30)
print(type(values)) # <class 'tuple'>
print(values[1]) # 20



# 创建一个元组
a_tuple = tuple(range(1, 10, 2))
print(a_tuple)    # (1, 3, 5, 7, 9)
# 序列解包: 将a_tuple元组的各元素依次赋值给a、b、c、d、e变量
a, b, c, d, e = a_tuple
print(a, b, c, d, e) # 1 3 5 7 9

# 定义一个列表
a_list = ['unitymarvel', 'UM']
# 序列解包: 将a_list序列的各元素依次赋值给a_str、b_str变量
a_str, b_str = a_list
print(a_str, b_str) # unitymarvel UM


# 将10、20、30依次赋值给x、y、z
x, y, z = 10, 20, 30
print(x, y, z) # 10 20 30
# 将y,z, x依次赋值给x、y、z
x, y, z = y, z, x
print(x, y, z) # 20 30 10
x = 20
y = 30


# first、second保存前2个元素，rest列表包含剩下的元素
first, second, *rest = range(10)
print(first) # 0
print(second) # 1
print(rest) # [2, 3, 4, 5, 6, 7, 8, 9]
# last保存最后一个元素，begin保存前面剩下的元素
*begin, last = range(10)
print(begin) # [0, 1, 2, 3, 4, 5, 6, 7, 8]
print(last) # 9
# first保存第一个元素，last保存最后一个元素，middle保存中间剩下的元素
first, *middle, last = range(10)
print(first) # 0
print(middle) # [0, 1, 2, 3, 4, 5, 6, 7, 8]
print(last) # 9
x,y = y,x
print(x,y)