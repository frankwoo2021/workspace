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
from pygame.locals import *
import sys
pygame.init()
screen = pygame.display.set_mode((600,500))
pygame.display.set_caption("绘制直线")
screen.fill((0, 0, 200))
pygame.draw.line(screen, (255, 255, 0), (100, 100), (500, 400), 12)
pygame.draw.line(screen, (255, 0, 0), (100, 200), (400, 200), 12)
pygame.display.update()
typeList = [QUIT]
while True:
    for event in pygame.event.get():
        if event.type in typeList:
            sys.exit()


