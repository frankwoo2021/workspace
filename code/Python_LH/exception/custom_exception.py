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

class WarpdriveOverloadException(Exception):
    pass

warpSpeed = 12

if warpSpeed >= 10:
    raise WarpdriveOverloadException("曲速引擎已经过载，请停止或弹出曲速核心，否则飞船将会爆炸")