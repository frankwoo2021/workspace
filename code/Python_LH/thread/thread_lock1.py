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


from atexit import register
import random
from threading import Thread, Lock, current_thread
from time import sleep, ctime

lock = Lock()
def fun():   
    lock.acquire()
    for i in range(5):

        print('Thread Name','=',current_thread().name,'i','=',i)
        sleep(random.randint(1,5))
    lock.release()
def main():
    for i in range(3):
        Thread(target=fun).start()
@register
def exit():
    print('线程执行完毕:', ctime())
if __name__ == '__main__':
    main()