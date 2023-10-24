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

import math
import pygame
from pygame.locals import *
import sys
pygame.init()
screen = pygame.display.set_mode((600,500))
pygame.display.set_caption("绘制弧形")

screen.fill((0, 0, 200))
# 绘制弧形
pygame.draw.arc(screen, (255, 0, 255), (200, 150, 200, 200), math.radians(0), math.radians(180), 10)
pygame.draw.arc(screen, (255, 255, 0), (240, 150, 240, 250), math.radians(90), math.radians(270), 18)
pygame.display.update()
typeList = [QUIT]
while True:
    for event in pygame.event.get():
        if event.type in typeList:
            sys.exit()


