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

'''
{
}

'''

name = input("请输入您的名字：")		#  从控制台输入名字
if name.startswith("B"):				#  if代码块
    print("名字以B开头")
    print('hello world')
elif name.startswith("F"):				#  elif代码块
    print("名字以F开头")
elif name.startswith("T"):				#  elif代码块
    print("名字以T开头")
else:									#  else代码块
    print("名字以其他字母开头")
