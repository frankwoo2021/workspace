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


from threading import BoundedSemaphore

MAX = 3
semaphore = BoundedSemaphore(MAX)
print(semaphore._value)
semaphore.acquire()
print(semaphore._value)
semaphore.acquire()
print(semaphore._value)
semaphore.acquire()
print(semaphore._value)
print(semaphore.acquire(False))

print(semaphore._value)
semaphore.release()
print(semaphore._value)
semaphore.release()
print(semaphore._value)
semaphore.release()
print(semaphore._value)
#semaphore.release()


