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
import datetime

def myResponse(request):
    return HttpResponse('<h1>hello world</h1>',content_type="text/html")
def writeCookie(request):
    dt = datetime.datetime.now() + datetime.timedelta(seconds=int(20))
    response = HttpResponse('writeCookie')
    response.set_cookie('name', 'Bill',expires=dt)
    response.set_cookie('age', 30)
    return response
def readCookie(request):
    result = ''
    name = str(request.COOKIES.get("name"))
    age = str(request.COOKIES.get('age'))
    result = '<h2>name:<font color="red">' + name + '</font></h2>'
    result += '<h2>age:<font color="blue">' + age + '</font></h2>'
    return HttpResponse(result,content_type="text/html")

