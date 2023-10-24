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
def fun(index, sec,lock):
    print('开始执行', index,'执行时间：',ctime())
    sleep(sec)
    print('执行结束',index,'执行时间：',ctime())
    lock.release()

def main():
    lock1 = thread.allocate_lock()
    lock1.acquire()
    thread.start_new_thread(fun, 
            (10, 4, lock1))
    lock2 = thread.allocate_lock()
    lock2.acquire()
    thread.start_new_thread(fun, 
            (20, 2, lock2))
    while lock1.locked() or lock2.locked():
        pass    
if __name__ == '__main__':
    main()
