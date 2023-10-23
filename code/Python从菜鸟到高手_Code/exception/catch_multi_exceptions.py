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

class NegativeException(Exception):
    pass
class ZeroException(Exception):
    pass

class SpecialCalc:
    def add(self,x,y):
        if x < 0 or y < 0:
            raise NegativeException
        return x + y
    def sub(self,x,y):
        if x - y < 0:
            raise NegativeException
        return x - y
    def mul(self,x,y):
        if x == 0 or y == 0:
            raise ZeroException
        return x * y
    def div(self,x,y):
        return x / y

while True:
    try:
        calc = SpecialCalc()
        expr = input("请输入要计算的表达式，例如，add(1,2)：")
        if expr == ":exit":
            break;
        result = eval('calc.' + expr)
        print("计算结果：{:.2f}".format(result))
    except NegativeException:
        print("******负数异常******")
    except ZeroException:
        print("******操作数为0异常******")
    except ZeroDivisionError:
        print("******分母不能为0******")    
    except:
        print("******其他异常******")
        