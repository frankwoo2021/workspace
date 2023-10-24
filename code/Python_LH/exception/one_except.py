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

class CustomException1(Exception):
    pass
class CustomException2(Exception):
    pass
class CustomException3(Exception):
    pass
import random


def raiseException():
    n = random.randint(1,3)
    print("抛出CustomException{}异常".format(n))
    if n == 1:
        raise CustomException1
    elif n == 2:
        raise CustomException2
    else:
        raise CustomException3
try:
    raiseException()
except (CustomException1,CustomException2,CustomException3):
    print("******执行异常处理程序******") 