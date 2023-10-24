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
def writeSession(request):
    request.session['name'] = 'Bill'
    request.session['age']  =20
    return HttpResponse('writeSession')
def readSession(request):
    result = ''
    name = request.session.get('name')
    age = request.session.get('age')
    if name:
        result = '<h2>name:<font color="red">' + name + '</font></h2>'
    if age:
        result += '<h2>name:<font color="blue">' + str(age) + '</font></h2>'
    return HttpResponse(result,content_type="text/html")

