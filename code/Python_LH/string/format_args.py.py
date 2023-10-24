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



print("原样输出：{first:s}  调用repr函数：{first!r}  输出Unicode编码：{first!a}".format(first = "中"))
print("整数：{num}  浮点数：{num:f}".format(num = 21))
print("十进制：{num}  二进制：{num:b}  八进制：{num:o}  十六进制：{num:x}".format(num = 56))
print("科学计数法：{num:e}".format(num = 533))
print("百分比：{num:%}".format(num = 0.56))
print("{:F}  {:f}".format(float("nan"),float("inf")))



