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

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def myPost(request):
    user = str(request.POST.get('user'))
    age = str(request.POST.get('age'))
    result = '<h2>name:<font color="red">' + user + '</font></h2>'
    result += '<h2>age:<font color="blue">' + age + '</font></h2>'
    return HttpResponse(result)