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

import sys, pygame
from pygame.locals import *

def showText(font, x, y, text, color=(255,255,255)):
    imgText = font.render(text, True, color)
    screen.blit(imgText, (x,y))

pygame.init()
screen = pygame.display.set_mode((200,200))
pygame.display.set_caption("键盘演示")
myfont = pygame.font.Font('simfang.ttf', 30)

showText(myfont, 100, 100, "按下左箭头")

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[K_ESCAPE] or keys[K_RETURN]:
        sys.exit()
    screen.fill((0,100,0))
    if keys[K_LEFT]:
        showText(myfont, 20, 100, "按下左箭头")
    if keys[K_RIGHT]:
        showText(myfont, 20, 100, "按下右箭头")

    pygame.display.update()

    

