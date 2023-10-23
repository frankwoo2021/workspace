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
screen = pygame.display.set_mode((600,500))
pygame.display.set_caption("绘制圆")
screen.fill((0, 0, 200))

pygame.draw.circle(screen, (255, 255, 0), (200, 250), 120, 12)
pygame.draw.circle(screen, (0, 255, 0), (300, 350), 100, 12)
pygame.draw.circle(screen, (255, 0, 0), (300, 150), 100, 12)
pygame.draw.circle(screen, (255, 255, 255), (440, 250), 120, 12)
pygame.display.update()
typeList = [QUIT]
while True:
    for event in pygame.event.get():
        if event.type in typeList:
            sys.exit()



