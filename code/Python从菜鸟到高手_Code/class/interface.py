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
    def method1(self):
        print("method1")
    def default(self):
        print("default")
my = MyClass()
if hasattr(my, 'method1'):
    # 运行结果：method1
    my.method1()
else:
    print("method2方法不存在")
if hasattr(my,'method2'):
    my.method2()
else:
    print("method2方法不存在")

method = getattr(my, 'method2',my.default)
method()

def method2():
    print("动态添加的method2")
setattr(my, 'method2', method2)
my.method2()

    
  
