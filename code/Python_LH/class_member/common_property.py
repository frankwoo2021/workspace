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

class Rectangle:
    def __init__(self):
        self.left = 0
        self.top = 0
    def setPosition(self,position):
        self.left,self.top = position
    def getPosition(self):
        return self.left,self.top

r = Rectangle()
r.left = 10
r.top = 20
print('left','=',r.left)
print('top','=',r.top)
r.setPosition([30,50])
print('position', '=', r.getPosition())

