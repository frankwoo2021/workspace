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

#raise Exception
#raise Exception("这是自己主动抛出的一个异常")
#raise ArithmeticError
#raise ArithmeticError("这是一个和数值有关的异常")
from boto.codedeploy.exceptions import InvalidRoleException
raise InvalidRoleException(2,"这是一个和Role有关的异常")

