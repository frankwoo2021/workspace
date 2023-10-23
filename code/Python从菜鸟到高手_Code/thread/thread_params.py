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

import random
from time import sleep
import _thread as thread
def fun(a,b):
    print(a,b)
    sleep(random.randint(1,5))
for i in range(8):
    thread.start_new_thread(fun, (i + 1,'a' * (i + 1)))
input()