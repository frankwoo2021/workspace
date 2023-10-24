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

x = 1                # 全局变量
def fun1():
    #global x
    x = 30          # 局部变量
fun1()
# 运行结果：1
print(x)

x = 123                # 全局变量
def fun2():
    print(x)            # 运行结果：123
fun2()

x = 123
def fun3():
    x = 30
    print(x)            # 运行结果：30
fun3()

x = 123
def fun4():
    #global x
    print(x)  # 执行这行代码会抛出异常
    x = 30

fun4()

x = 30
def fun5():
    x = 40
    # 嵌套函数
    def fun6():
        # 这里的变量x是在函数fun5中定义的局部变量
        print(x)
        print("fun6")
    # 返回fun6函数本身
    return fun6
fun5()()        # 调用了fun5函数的嵌套函数fun6
