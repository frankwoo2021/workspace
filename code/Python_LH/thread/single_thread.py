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

from time import sleep, ctime

def fun1():
    print('开始运行fun1:', ctime())
    sleep(4)
    print('fun1运行结束:', ctime())

def fun2():
    print('开始运行fun2:', ctime())
    sleep(2)
    print('fun2运行结束:', ctime())

def main():

    print('开始运行时间:', ctime())
    fun1()
    fun2()
    print('结束运行时间:', ctime())    

if __name__ == '__main__':
    main()
