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

from collections import deque

q = deque(range(10))
print(q)
q.append(100)
q.append(-100)
print(q)
q.appendleft(20)
print(q)
print(q.pop())
print(q)
print(q.popleft())
print(q)
q.rotate(-2)
print(q)
q.rotate(4)
print(q)
q1 = deque(['a','b'])
q.extend(q1)
print(q)
q.extendleft(q1)
print(q)
