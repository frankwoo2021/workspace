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


import _thread as thread
from time import sleep, ctime
import random
from threading import currentThread
def fun():
    for i in range(10):
        print(currentThread().name,i)
        sleep(random.randint(1,5))
def main():
    thread.start_new_thread(fun, ())
    thread.start_new_thread(fun, ())
    input()
if __name__ == '__main__':
    main()
