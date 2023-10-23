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

def abc():
    pass
print(abc())

def no_return(flag):
    print("这是在函数中打印的信息")
    if flag:
        return 
    print("这行信息只有在flag为False是才会输出")

no_return(False)
print("----------")
returnValue = no_return(True)

print(returnValue)