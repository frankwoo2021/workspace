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

import sys, pygame,math
from pygame.locals import *
import time
def wrapAngle(angle):
    return angle % 360
pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("围绕地球旋转的飞船")
font = pygame.font.Font('simfang.ttf', 18)

space = pygame.image.load("space.png").convert_alpha()
earth = pygame.image.load("earth.png").convert_alpha()
airship = pygame.image.load("airship.png").convert_alpha()
width,height = airship.get_size()
airship = pygame.transform.smoothscale(airship, (width//2, height//2))

radius = 250
angle = 0.0
airshipAngle = 0.0

x, y = 0, 0
oldX, oldY = 0, 0

count = 0
# 图像自转
def rotateCenter(image, angle):
    origRect = image.get_rect()
    rotateImage = pygame.transform.rotate(image, angle)
    rotateRect = origRect.copy()
    rotateRect.center = rotateImage.get_rect().center
    rotateImage = rotateImage.subsurface(rotateRect).copy()
    return rotateImage
# 绘制背景
screen.blit(space, (0,0))
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        sys.exit()


    # 绘制地球
    count += 1
    if count == 100:
        # 绘制背景
        screen.blit(space, (0, 0))
        angle = wrapAngle(angle)
        scratchEarth = rotateCenter(earth, angle)
        angle += 1
        width, height = earth.get_size()
        screen.blit(scratchEarth, (400 - width / 2, 300 - height / 2))
        count = 0

    # 移动飞船
    airshipAngle = wrapAngle(airshipAngle - 0.02)
    x = math.sin(math.radians(airshipAngle)) * radius
    y = math.cos(math.radians(airshipAngle)) * radius

    # 旋转飞船
    deltaX = x - oldX
    deltaY = y - oldY
    rangle = math.atan2(deltaY, deltaX)
    rangled = wrapAngle(-math.degrees(rangle))

    scratchAirShip = pygame.transform.rotate(airship, rangled)

    # 绘制飞船
    width, height = scratchAirShip.get_size()
    newX = 400 + x - width // 2
    newY = 300 + y - height // 2
    screen.blit(scratchAirShip, (newX, newY))
    pygame.display.update()

    oldX = x
    oldY = y


