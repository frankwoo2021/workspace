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


class ParentClass:
    name = 30
    def method1(self):
        print("method1")
class ChildClass(ParentClass):
    def method2(self):
        print("method2")
        print(self.name)

child = ChildClass()
child.method1()
child.method2()
        
