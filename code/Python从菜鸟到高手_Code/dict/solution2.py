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


s = input("请输入一个包含整数的字符串：")
s1 = ""
number = ""
index = 0
dict = {}
for i in range(len(s)):
    c = s[i]
    if ord(c) in range(48,58):
        number += c
    else:
        if len(number) > 0:            
            s1 += "{{number{}:010}}".format(index)
            dict["number" + str(index)] = int(number)
            index += 1
            number = ""
        s1 += c
# 处理以数字结尾的情况
if len(number) > 0:            
    s1 += "{{number{}:010}}".format(index)
    dict["number" + str(index)] = int(number)            
print(s1)
print(s1.format_map(dict))
