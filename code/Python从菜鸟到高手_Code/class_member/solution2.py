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

class Factorial:
    def __init__(self):
        self.result = 1
        self.n = 0
    def __next__(self):
        if self.n == 0 or self.n == 1:
            self.n += 1
            self.result = 1
        else:
            self.result = self.result * (self.n)
            self.n += 1
        if self.result > 100000: raise StopIteration
        return self.result
    def __iter__(self):
        return self
    def reset(self):
        self.result = 1
        self.n = 0

factorial = Factorial()
print(list(factorial))   # 转换为序列