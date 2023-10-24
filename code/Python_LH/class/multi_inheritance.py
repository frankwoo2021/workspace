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

class Calculator:
    def calculate(self,expression):
        self.value = eval(expression)
    def printResult(self):
        print("result:{}".format(self.value))

    
class MyPrint:
    def printResult(self):
        print("计算结果：{}".format(self.value))
    def aa(self,a):
        return 30
class NewCalculator(Calculator, MyPrint):
    pass
class NewCalculator1(MyPrint,Calculator):
    pass
calc = NewCalculator()
calc.calculate("1 + 3 * 5")
calc.printResult()
print(NewCalculator.__bases__)

calc1 = NewCalculator1()
print(NewCalculator1.__bases__)
calc1.calculate("1 + 3 * 5")
calc1.printResult()


