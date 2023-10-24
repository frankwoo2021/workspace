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
def solution1(request):
    user = str(request.POST.get('user'))
    age = str(request.POST.get('age'))
    country = str(request.POST.get('country'))

    with open('form.txt','w') as f:
        f.writelines("user:%s\r\n" % user)
        f.writelines("age:%s\r\n" % age)
        f.writelines("country:%s" % country)
    return HttpResponse('Form has been written to the server')
