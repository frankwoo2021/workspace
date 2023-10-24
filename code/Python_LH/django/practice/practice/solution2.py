#########################################################################
# 作者:李宁（蒙娜丽宁）
#
# 微信公众号：极客起源
#
# B站：https://space.bilibili.com/477001733
#
# Copyright © 2022 Lining. All rights reserved.
#
# 版本: 2.0
#########################################################################

from django.shortcuts import render
class MyClass:
    def __init__(self,name,age):
        self.name = name
        self.age = age
def solution2(request):
    values = {'values':[MyClass('Bill',20),MyClass('Mike',30),MyClass('John',12)]}
    return render(request, 'for.html', values)