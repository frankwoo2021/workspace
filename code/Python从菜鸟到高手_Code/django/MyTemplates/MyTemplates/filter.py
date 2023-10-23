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

from django.shortcuts import render

def myFilter(request):
    values = {}
    values['value1'] = 'hello'

    values['value2'] = 'WORLD'
    values['value3'] = 'abcdefg'
    return render(request, 'filter.html', values)