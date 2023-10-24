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

import os							# 导入os模块
import sys							# 导入sys模块
f_handler=open('out.log', 'w')		# 打开out.log文件
oldstdout = sys.stdout				# 保存默认的Python标准输出
sys.stdout=f_handler				# 将Python标准输出指向out.log
os.system('cls')					# 清空Python控制台
sys.stdout = oldstdout				# 恢复Python默认的标准输出
