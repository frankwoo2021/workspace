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


print("HEllo".lower())
print("hello".upper())
list = ["Python", "Ruby", "Java", "KOTLIN"]
if "Kotlin" in list:
    print("找到Kotlin了")
else:
    print("未找到Kotlin")

for lang in list:
    if "kotlin" == lang.lower():
        print("找到Kotlin了")
        break;
s = "i not only like Python, but also like Kotlin."
import string
print(string.capwords(s))