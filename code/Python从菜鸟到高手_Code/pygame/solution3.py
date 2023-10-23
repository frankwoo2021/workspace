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

import random, math, pygame
from pygame.locals import *
import sys


pygame.init()
screen = pygame.display.set_mode((600,500))
pygame.display.set_caption("彩色圆环")
screen.fill((0,0,100))

posX = 300
posY = 250
radius = 200
smallRadius = 20
angle = 0


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        sys.exit()
    for k in range(1,10):
        if keys[K_0 + k]:
            screen.fill((0, 0, 100))
            smallRadius = 5 * k
            break

    angle += 1
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = r,g,b

    x = math.cos( math.radians(angle) ) * radius
    y = math.sin( math.radians(angle) ) * radius

    pos = ( int(posX + x), int(posY + y) )
    pygame.draw.circle(screen, color, pos, smallRadius)


    pygame.display.update()

    

