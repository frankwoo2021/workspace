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


def sortNumbers(*numbers,type="asc"):
    if type == "asc":
        return sorted(numbers)
    else:
        return sorted(numbers,reverse = True)

print(sortNumbers(6,5,3,8,4,3))
print(sortNumbers(6,5,3,8,4,3,type="desc"))
    