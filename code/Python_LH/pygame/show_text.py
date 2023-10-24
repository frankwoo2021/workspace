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

yellow = (255,255,0)
blue = (0,0,200)

pygame.init()
screen = pygame.display.set_mode((300,180))

myFont = pygame.font.Font('simfang.ttf',50)

textImage = myFont.render("你好 Pygame", True, yellow)
print(type(textImage))
typeList = [QUIT]
screen.fill(blue)
screen.blit(textImage, (10,60))
pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type in typeList:
            print('exit')
            sys.exit()



