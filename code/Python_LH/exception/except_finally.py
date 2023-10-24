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
    try:
        print("fun1 正常执行")
    finally:
        print("fun1 finally")
def fun2():
    try:
        raise Exception
    except:
        print("fun2 抛出异常")
    finally:
        print("fun2 finally")
def fun3():
    try:
        return 20
    finally:
        print("fun3 finally")
def fun4():
    try:
        x = 1/0
    except ZeroDivisionError as e:
        print(e)
    finally:
        print("fun4 finally")
        try:
            del x
        except Exception as e:
            print(e)


fun1()
fun2()
print(fun3())
fun4()