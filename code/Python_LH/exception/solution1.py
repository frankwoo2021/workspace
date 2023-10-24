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


class StartMobileException(Exception):
    pass
import random
class Mobile:
    
    def start(self):
        value = random.randint(1,100)
        if value < 50:
            raise StartMobileException('开机错误')

mobile = Mobile()
mobile.start()
                              