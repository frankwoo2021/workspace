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

numStr= input('请输入一个大于1的整数：')
n = int(numStr)
m = n * n
i = 1
numbers = []
values = []
# 通过循环产生二维列表
while i <= m:
    values.append(i)
    if i % n == 0:
        numbers.append(values.copy())
        values.clear()
    i += 1
print(numbers)
i = 0;
j = 1;
#  通过二重循环交互相应元素的值
while i < n:
    while j < n:
        if j < i:
            break
        numbers[i][j],numbers[j][i] =numbers[j][i],numbers[i][j]
        print(i,j,numbers[i][j],numbers[j][i])
        j+=1
    j = 1
    i+=1
print(numbers)