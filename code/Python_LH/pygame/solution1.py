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
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("请按1、2、3、4")
myfont = pygame.font.Font(None, 60)

color = 200, 80, 60
width = 4
x = 250
y = 250
radius = 200
position = x-radius, y-radius, radius*2, radius*2

piece1 = False
piece2 = False
piece3 = False
piece4 = False

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        elif event.type == KEYUP:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
            elif event.key == pygame.K_1:
                piece1 = True
            elif event.key == pygame.K_2:
                piece2 = True
            elif event.key == pygame.K_3:
                piece3 = True
            elif event.key == pygame.K_4:
                piece4 = True
                

    screen.fill((0,0,200))
    

    textImg1 = myfont.render("1", True, color)
    screen.blit(textImg1, (x+radius/2-20, y-radius/2))
    textImg2 = myfont.render("2", True, color)
    screen.blit(textImg2, (x-radius/2, y-radius/2))
    textImg3 = myfont.render("3", True, color)
    screen.blit(textImg3, (x-radius/2, y+radius/2-20))
    textImg4 = myfont.render("4", True, color)
    screen.blit(textImg4, (x+radius/2-20, y+radius/2-20))


    if piece1:
        startAngle = math.radians(0)
        endAngle = math.radians(90)
        pygame.draw.arc(screen, color, position, startAngle, endAngle, width)
        pygame.draw.line(screen, color, (x,y), (x,y-radius), width)
        pygame.draw.line(screen, color, (x,y), (x+radius,y), width)
    if piece2:
        startAngle = math.radians(90)
        endAngle = math.radians(180)
        pygame.draw.arc(screen, color, position, startAngle, endAngle, width)
        pygame.draw.line(screen, color, (x,y), (x,y-radius), width)
        pygame.draw.line(screen, color, (x,y), (x-radius,y), width)
    if piece3:
        startAngle = math.radians(180)
        endAngle = math.radians(270)
        pygame.draw.arc(screen, color, position, startAngle, endAngle, width)
        pygame.draw.line(screen, color, (x,y), (x-radius,y), width)
        pygame.draw.line(screen, color, (x,y), (x,y+radius), width)
    if piece4:
        startAngle = math.radians(270)
        endAngle = math.radians(360)
        pygame.draw.arc(screen, color, position, startAngle, endAngle, width)
        pygame.draw.line(screen, color, (x,y), (x,y+radius), width)
        pygame.draw.line(screen, color, (x,y), (x+radius,y), width)
        

    if piece1 and piece2 and piece3 and piece4:
        color = 0,255,0

    pygame.display.update()

