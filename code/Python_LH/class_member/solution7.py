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

def enumList(nestedList):
    try:
        try: nestedList + ''
        except TypeError:
            pass
        else:
            raise TypeError
        for subList in nestedList:
           for element in enumList(subList):
                yield element
    except TypeError:
        yield nestedList
nestedList = ['a',['b',['c'],20,123,[['hello world']]]]
for num in enumList(nestedList):
    print(num, end=' ')
