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


values1 = (1,3,"hello")
str1 = "abc %d,  xyz %d,  %s world" 
print(str1 % values1)

values2 = {'title':'极客起源', 'url':'https://geekori.com', 'company':'欧瑞科技'}

str2 = """
<html>
    <head>
        <title>{title}</title>
        <meta charset="utf-8" /> 
    <head>
    <body>
        <h1>{title}</h1>
        <a href="{url}">{company}</a>
    </body>
</html>
"""
print(str2.format_map(values2))

