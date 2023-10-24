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

class Person:
    def __init__(self,name = "Bill"):
        print("构造方法已经被调用")
        self.name = name
    def getName(self):
        return self.name
    def setName(self,name):
        self.name= name

person = Person()
print(person.getName())
person1 = Person(name = "Mike")
print(person1.getName())
person1.setName(name = "John")
print(person1.getName())