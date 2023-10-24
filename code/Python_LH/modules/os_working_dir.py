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

import os

# 获取系统信息
# 返回当前的工作目录
print('当前工作目录：',os.getcwd())
# 返回path指定的文件夹包含的文件或文件夹的名字的列表。
print('工作目录中包含的文件或文件夹的名字的列表')
print(os.listdir(os.getcwd()))
# 改变当前工作目录
os.chdir('../')
print('改变后的工作目录',os.getcwd())
print('新的工作目录中包含的文件或文件夹的名字的列表')
print(os.listdir(os.getcwd()))
