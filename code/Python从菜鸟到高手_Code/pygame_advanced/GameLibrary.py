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

import sys, time, random, math, pygame
from pygame.locals import *



def showText(font, x, y, text, color=(255, 255, 255)):
    imgText = font.render(text, True, color)
    screen = pygame.display.get_surface()  # req'd when function moved into MyLibrary
    screen.blit(imgText, (x, y))


# MySprite class extends pygame.sprite.Sprite
class MySprite(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)  # extend the base Sprite class
        self.masterImage = None
        self.frame = 0
        self.oldFrame = -1
        self.frameWidth = 1
        self.frameHeight = 1
        self.firstFrame = 0
        self.lastFrame = 0
        self.columns = 1
        self.lastTime = 0
        self.direction = 0
        self.velocity = Point(0.0, 0.0)

        # X property

    def _getx(self):
        return self.rect.x

    def _setx(self, value):
        self.rect.x = value

    X = property(_getx, _setx)

    # Y property
    def _gety(self):
        return self.rect.y

    def _sety(self, value):
        self.rect.y = value

    Y = property(_gety, _sety)

    # position property
    def _getpos(self):
        return self.rect.topleft

    def _setpos(self, pos):
        self.rect.topleft = pos

    position = property(_getpos, _setpos)

    def load(self, filename, columns=1, width=0, height=0):
        self.masterImage = pygame.image.load(filename).convert_alpha()
        masterRect = self.masterImage.get_rect()
        if width == 0:
            width = masterRect.width
        if height == 0:
            height = masterRect.height
        self.frameWidth = width
        self.frameHeight = height

        self.rect = Rect(0, 0, width, height)
        self.columns = columns
        # try to auto-calculate total frames
        rect = self.masterImage.get_rect()
        self.lastFrame = (rect.width // width) * (rect.height // height) - 1

    def update(self, current_time = 0, rate=30):
        # update animation frame number
        if current_time > self.lastTime + rate:
            self.frame += 1
            if self.frame > self.lastFrame:
                self.frame = self.firstFrame
            self.lastTime = current_time

        # build current frame only if it changed
        if self.frame != self.oldFrame:
            frameX = (self.frame % self.columns) * self.frameWidth
            frameY = (self.frame // self.columns) * self.frameHeight
            rect = Rect(frameX, frameY, self.frameWidth, self.frameHeight)
            self.image = self.masterImage.subsurface(rect)
            self.oldFrame = self.frame

    def __str__(self):
        return str(self.frame) + "," + str(self.firstFrame) + \
               "," + str(self.lastFrame) + "," + str(self.frameWidth) + \
               "," + str(self.frameHeight) + "," + str(self.columns) + \
               "," + str(self.rect)


# Point class
class Point(object):
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    # X property
    def getx(self): return self.__x

    def setx(self, x): self.__x = x

    x = property(getx, setx)

    # Y property
    def gety(self): return self.__y

    def sety(self, y): self.__y = y

    y = property(gety, sety)

    def __str__(self):
        return "{X:" + "{:.0f}".format(self.__x) + \
               ",Y:" + "{:.0f}".format(self.__y) + "}"

