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

s = input("请输入一个大字符串：")

while True:
    subString = input("请输入一个子字符串：")
    if subString == "end":
        break 
    startStr = input("请输入开始索引：")
    endStr = input("请输入结束索引：")
    start = 0
    end = len(s)
      
    if startStr != "":
        start = int(startStr)
    if endStr != "":
        end = int(endStr)
    print("'{}'在'{}'的出现的位置是{}：".format(subString, s,s.find(subString,start,end)))