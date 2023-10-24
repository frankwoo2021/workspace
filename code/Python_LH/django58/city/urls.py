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

urlpatterns = [
    url(r'^hello$', view.hello),
    url(r'^$', view.index),
    url(r'^index/$', view.index),
    url(r'^login/$', view.login),
    url(r'^logout/$', view.logout),
    url(r'^register/$', view.register),
    url(r'^recruitment/$', view.recruitment),
    url(r'^recList/$', view.recList),
    url(r'^apply/$', view.apply),
    url(r'^recDetails/$', view.recDetails),
    url(r'^carList/$', view.carList),
    url(r'^carAjaxInfo/$', view.carAjaxInfo),
]