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

scope = {}
codes = ""						# 用于保存输入的所有代码
print(">>>",end="")			# 输出Python控制台提示符
while True:
    code= input("")				# 输入每一行代码
    if code == "":				# 如果输入的是空串，会执行以前输入的所有Python代码
        exec(codes, scope)		# 执行以前输入的所有Python代码
        codes = ""                  # 重置codes变量，以便重新输入Python代码
        print(">>>",end="")		# 继续输出Python控制台提示符
        continue   				# 忽略后面的代码
    codes += code + "\n"		# 将输入的每一行代码收尾连接，中间换行
