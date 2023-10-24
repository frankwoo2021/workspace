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
screen = pygame.display.set_mode((500,300))
pygame.display.set_caption("鼠标演示")
myFont = pygame.font.Font('simfang.ttf', 20)
white = 255,255,255

seconds = 10
score = 0
mouseX = mouseY = 0
moveX = moveY = 0
mouseDown = mouseUp = 0
mouseDownX = mouseDownY = 0
mouseUpX = mouseUpY = 0


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        elif event.type == MOUSEMOTION:
            mouseX,mouseY = event.pos
            moveX,moveY = event.rel
        elif event.type == MOUSEBUTTONDOWN:
            mouseDown = event.button
            mouseDownX,mouseDownY = event.pos
        elif event.type == MOUSEBUTTONUP:
            mouseUp = event.button
            mouseUpX,mouseUpY = event.pos

    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        sys.exit()

    screen.fill((0,100,0))

    showText(myFont, 0, 0, "鼠标事件")
    showText(myFont, 0, 20, "鼠标位置: " + str(mouseX) +
               "," + str(mouseY))
    showText(myFont, 0, 40, "鼠标相对位置: " + str(moveX) +
               "," + str(moveY))

    showText(myFont, 0, 60, "鼠标按钮按下: " + str(mouseDown) +
               " at " + str(mouseDownX) + "," + str(mouseDownY))

    showText(myFont, 0, 80, "鼠标按钮抬起: " + str(mouseUp) +
               " at " + str(mouseUpX) + "," + str(mouseUpY))

    showText(myFont, 0, 160, "鼠标检测")
    
    x,y = pygame.mouse.get_pos()
    showText(myFont, 0, 180, "鼠标位置: " + str(x) + "," + str(y))

    b1, b2, b3 = pygame.mouse.get_pressed()
    showText(myFont, 0, 200, "鼠标按钮状态: " +
               str(b1) + "," + str(b2) + "," + str(b3))
    
    pygame.display.update()

    

