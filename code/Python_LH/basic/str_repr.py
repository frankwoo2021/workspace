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


# 输出带“\n"的字符串，运行结果：<hello
#							 world>
print("<hello\nworld>")
# 用str函数将1234转换为数字，运行结果：1234
print(str(1234))
# 抛出异常，len函数不能直接获取数字的长度
#print(len(1234))
#  将1234转换为字符串后，获取字符串长度，运行结果：4
print(len(str(1234)))
#  运行结果：<hello
#			 world>
print(str("<hello\nworld>"))
#  运行结果：13
print(len(str("<hello\nworld>")))
#  运行结果：'<hello\nworld>'
print(repr("<hello\nworld>"))
#  运行结果：16
print(len(repr("<hello\nworld>")))
#  使用转义符输出“\”，输出的字符串不会用单引号括起来，运行结果：hello\nworld
print("<hello\\nworld>")
#  运行结果：14
print(len("<hello\\nworld>"))
#  在字符串前面加“r”，保持字符串原始格式输出，运行结果：hello\nworld
print(r"<hello\nworld>")
#  运行结果：14
print(len(r"<hello\nworld>"))
