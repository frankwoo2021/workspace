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
import time
def wrapAngle(angle):
    return angle % 360
pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("旋转的地球")
font = pygame.font.Font('simfang.ttf', 18)

space = pygame.image.load("space.png").convert_alpha()
earth = pygame.image.load("earth.png").convert_alpha()
angle = 0.0
# 图像自转
def rotateCenter(image, angle):
    origRect = image.get_rect()
    rotateImage = pygame.transform.rotate(image, angle)
    rotateRect = origRect.copy()
    rotateRect.center = rotateImage.get_rect().center
    rotateImage = rotateImage.subsurface(rotateRect).copy()
    return rotateImage
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        sys.exit()

    # 绘制背景
    screen.blit(space, (0,0))
    # draw planet
    width, height = earth.get_size()

    angle = wrapAngle( angle)

    scratchEarth = rotateCenter(earth,  angle)
    angle+=1

    screen.blit(scratchEarth, (400 - width / 2, 300 - height / 2))

    pygame.display.update()


    time.sleep(0.1)


