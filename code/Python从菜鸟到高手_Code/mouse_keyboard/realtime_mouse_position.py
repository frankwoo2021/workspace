#########################################################################
# 作者:李宁（蒙娜丽宁）
#
# 微信公众号：极客起源
#
# B站：https://space.bilibili.com/477001733
#
# Copyright © 2022 Lining. All rights reserved.
#
# 版本: 2.0
#########################################################################
import pyautogui
print('按Ctrl-C退出')
try:
    while True:
        x,y=pyautogui.position()
        positionStr = 'X:' + str(x).rjust(4)+ 'Y:'.rjust(4) + str(y).rjust(4)
        print(positionStr)
except KeyboardInterrupt:
    print('\n')
