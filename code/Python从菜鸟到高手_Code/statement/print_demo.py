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

#  输出用空格分隔的多参数值
print("name =", "Bill")
#  输出用空格分隔的多参数值
print("age =", 30)
#  使用加号（+）连接字符串
print("Apple" + "," + "Orange" + "," + "Banana")
#  修改多参数值分隔符为逗号（,），然后输出多参数值
print("Apple", "Orange","Banana", sep=",")
#  修改多参数值分隔符为“&”，然后输出多参数值
print("Can","you","tell","me", "how", "to", "get", "to","the","nearest", "tube", "station", sep="&")
#  修改输出字符串结尾符为空格，这样下一次调用print函数，就会中同一行输出内容了
#  运行结果：Hello world
print("Hello", end=" ")
print("world")
# 修改输出字符串结尾符为长度为0的字符串，这样下一次调用print函数，输出的内容不仅会在同一行，
# 而且会首尾相接，运行结果：abc
print("a",end="");
print("b",end="");
print("c");
