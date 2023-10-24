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

class JCException(Exception):
    pass
class JC:
    def compute(self, n):
        if n < 0:
            raise JCException('只能计算0或正整数的阶乘！')
        if n == 0 or n == 1:
            return 1
        else:
            return n * self.compute(n - 1)
jc = JC()
print(jc.compute(10))
try:
    print(jc.compute(-10))
except JCException as e:
    print(e)
    