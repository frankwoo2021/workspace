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

from django.http import HttpResponse


def hello(request):
    return HttpResponse("Hello world ! ")
def your(request):
    return HttpResponse('your')
def product(request):
    return HttpResponse('product')
def country(request):
    return HttpResponse('country')