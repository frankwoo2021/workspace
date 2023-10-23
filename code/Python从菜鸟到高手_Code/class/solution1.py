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
    name = None
    def walk(self):
        print("walk")
class Teacher(Person):
    def getField(self):
        print("我教的是化学")
class Student(Person):
    def test(self):
        print("我最讨厌考试")

teacher = Teacher()
teacher.walk()
teacher.getField()

student = Student()
student.walk()
student.test()