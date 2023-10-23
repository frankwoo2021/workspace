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

name = input("你叫什么名字？")			#  从Python控制台输入一个字符串（姓名）
if  name.startswith("Bill"):			#  以Bill开头的姓名
    if name.endswith("Gates"):			#  以Gates结尾的姓名（嵌套代码块）
        print("欢迎Bill Gates先生")
    elif name.endswith("Clinton"):		#  以Clinton结尾的姓名
        print("欢迎克林顿先生")
    else:								#  其他姓名
        print("未知姓名")
    print('hello world')
elif name.startswith("李"):				#  以“李”开头的姓名
    if name.endswith("宁"):				#  以“宁”结尾的姓名
        print("欢迎李宁老师")
    else:								#  其他姓名
        print("未知姓名")
else:									#  其他姓名
    print("未知姓名")
