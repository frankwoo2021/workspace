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
import sys
import os
import re
# 从标准输入读取全部数据
text = sys.stdin.read()

# 将字符串形式的文件和目录列表按行拆分，然后保存到列表中
files = text.split(os.linesep)
for file in files:
    if file.startswith('test'):
        print(file)

