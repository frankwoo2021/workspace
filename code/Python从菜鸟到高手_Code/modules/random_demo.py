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

import random
print(random.randint(1,100))
print(random.random())
# [1,4,7,10,13,16,19]选一个
print(random.randrange(1, 20, 3))
print(random.uniform(1, 100.5))
intList = [1,2,3,4,5,6,7,8,9,'a','b','c','d']
print(random.choice(intList))
newList = random.sample(intList, 3) 
print(newList)
random.shuffle(intList)
print(intList)
