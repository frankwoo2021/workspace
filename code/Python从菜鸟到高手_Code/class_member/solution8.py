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

def abc(f):
    ok = f()
    print('x:',ok.x)
    f.x = f.x*2
    return f
@abc
class MyClass:
    x = 20

my = MyClass()

print('y:',my.x)
