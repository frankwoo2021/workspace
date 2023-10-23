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


def myRequest(request):

    response = 'scheme:' + request.scheme + '<br>'
    response += 'path:' + request.path + '<br>'
    response += 'method:' + request.method + '<br>'
    response += 'HTTP_ACCEPT:' + request.META['HTTP_ACCEPT'] + '<br>'
    response += 'HTTP_USER_AGENT:' + request.META['HTTP_USER_AGENT'] + '<br>'
    response += 'REMOTE_ADDR:' + request.META['REMOTE_ADDR'] + '<br>'
    response += 'QUERY_STRING:' + request.META['QUERY_STRING'] + '<br>'
    response += 'name:' + str(request.GET['name'])+ '<br>'
    response += 'age:' + str(request.GET.get('age')) + '<br>'

    return HttpResponse(response)
