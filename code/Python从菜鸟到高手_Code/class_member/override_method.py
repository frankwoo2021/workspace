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

class Bird:
    def __init__(self):
        self.hungry= True
    def eat(self):
        if self.hungry:
            print("已经吃了虫子！")
            self.hungry = False
        else:
            print("已经吃过饭了，不饿了！")
b = Bird()
b.eat()
b.eat()

class SongBird(Bird):
    def __init__(self):
        self.sound = '向天再借五百年'
    def sing(self):
        print(self.sound)
    def eat1(self):
        print("SongBird eat")
        
sb = SongBird()
sb.sing()
sb.eat()