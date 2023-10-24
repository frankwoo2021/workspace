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


class MyClass:
    def getName(self):
        return self.name
    def setName(self, name):
        self.name = name
        self.__outName()
    # private method
    def __outName(self):
        print("Name = {}".format(self.name))        


myClass = MyClass()
import inspect
methods = inspect.getmembers(myClass, predicate=inspect.ismethod)
print(methods)
for method in methods:
    print(method[0])
print("------------")
myClass.setName("Bill")
print(myClass.getName())
myClass._MyClass__outName()
print(myClass.__outName())

