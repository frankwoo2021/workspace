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
if os.path.exists('data.txt') and not os.path.exists('slink.txt'):
    os.symlink('data.txt','slink.txt')
if os.path.exists('data.txt') and not os.path.exists('link.txt'):
    os.link('data.txt','link.txt')
