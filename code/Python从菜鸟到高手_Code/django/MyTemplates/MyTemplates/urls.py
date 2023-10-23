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

from django.conf.urls import url
from . import view
from . import condition
from . import iteration
from . import filter

urlpatterns = [
    url(r'^hello$', view.hello),
    url(r'^condition$', condition.myCondition),
    url(r'^for$', iteration.myFor),
    url(r'^filter$',filter.myFilter)
]
