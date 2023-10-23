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
print(dict.items())
for key_value in dict.items():
    print("key","=",key_value[0],"value","=",key_value[1])
print(("bike","自行车") in dict.items())

dict_items = dict.items()
dict["bike"] = "自行车； 摩托车； 电动自行车；"
print(dict_items)

print(dict.keys())
for key in dict.keys():
    print(key)