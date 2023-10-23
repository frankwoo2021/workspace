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
import time
pygame.init()
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("移动矩形")

posX = 300
posY = 250
velX = 2
velY = 1

typeList = [QUIT]
while True:
    for event in pygame.event.get():
        if event.type in typeList:
            sys.exit()

    screen.fill((0, 0, 200))
    # 改变矩形的坐标
    posX += velX
    posY += velY
    
    # 让矩形仍然在屏幕上（阻止矩形超出屏幕范围）
    if posX > 400 or posX < 0:
        velX = -velX
    if posY > 400 or posY < 0:
        velY = -velY
    
    # 绘制矩形
    pygame.draw.rect(screen, (255,255,0), ( posX, posY, 100, 100), 0)
    time.sleep(0.01)

    pygame.display.update()
