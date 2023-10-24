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


dict = {"help":"帮助", "bike":"自行车", "geek":"极客","China":"中国"}
while True:
    word = input("请输入英文单词：")
    if word == ":exit":
        break;
    value = dict.get(word)
    if value == None:
        print("{}在字典中不存在.".format(word))
    else:
        print("“{}”的含义是“{}”".format(word, value))

