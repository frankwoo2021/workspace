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

import pygame
import sys
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((600, 600))
typeList = [QUIT]
while True:
    for event in pygame.event.get():
        if event.type in typeList:
            sys.exit()




