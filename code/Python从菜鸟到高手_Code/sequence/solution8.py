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

account = [						# 保存了多条用户记录的序列
    ["geekori", "123456"],
    ["bill", "54321"],
    ["superman", "65432"],
    ["androidguy","6543"],
    ["unitymarvel", "123456"]
]

username = input("用户名：")			# 要求输入用户名
password = input("密码：")			# 要求输入密码
# 用in运算符判断一个序列是否属于account
if [username, password] in account:
    print("登录成功")
else:
    print("登录失败")
