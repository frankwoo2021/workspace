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

url = input("请输入一个Https网址：")
scheme = url[0:5]					#  分片获取Url中的Scheme
host = url[8:]						#  分片获取Url中的Host

print("scheme:", scheme)
print("host:",host)

