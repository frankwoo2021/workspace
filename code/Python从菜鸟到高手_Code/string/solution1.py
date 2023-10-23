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


s = input("请输入一个字符串：")
while True:
    subStr = input("请输入要统计的字符串：")
    if subStr == "end":
        break;
    i = 0
    count = 0
    while i < len(s):
        index = s.find(subStr, i)
        if index > -1:
            count += 1
            i = index + len(subStr)
        else:
            break;
    
    print("'{}'在'{}'中出现了{}次".format(subStr, s, count))
