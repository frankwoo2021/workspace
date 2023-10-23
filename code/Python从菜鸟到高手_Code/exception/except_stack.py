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

def fun1():
    raise Exception("fun1抛出的异常")
def fun2():
    fun1()
def fun3():
    fun2()
def fun4():
    fun3()
def fun5():
    fun4()

fun5()