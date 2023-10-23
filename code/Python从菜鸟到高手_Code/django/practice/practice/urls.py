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

from django.conf.urls import url
from . import solution1
from . import solution2
urlpatterns = [
    url(r'^solution1$', solution1.solution1),
    url(r'^solution2$', solution2.solution2),
]
