#########################################################################
# 作者:李宁（蒙娜丽宁）
#
# 微信公众号：极客起源
#
# B站：https://space.bilibili.com/477001733
#
# Copyright © 2022 Lining. All rights reserved.
#
# 版本: 2.0
#########################################################################


#  定义字符串模板
formatStr = "Hello %s. Today is %s, Are there any activities today?"
#  初始化字符串模板参数值，此处必须使用元组，不能使用列表
values = ('Mike', 'Wednesday')
#  格式化字符串
print(formatStr % values)
