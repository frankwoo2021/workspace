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

import sys,  pygame
from pygame.locals import *

class MySprite(pygame.sprite.Sprite):
    def __init__(self, target):
        pygame.sprite.Sprite.__init__(self)  # extend the base Sprite class

        self.frame = 0
        self.oldFrame = -1
        self.lastTime = 0
        self.firstFrame = 0
        self.lastFrame = 0

    def load(self, filename, width, height, columns, scale = 1):
        width = width * scale
        height = height * scale
        self.masterImage = pygame.image.load(filename).convert_alpha()
        imageWidth,imageHeight = self.masterImage.get_size()
        self.masterImage = pygame.transform.smoothscale(self.masterImage, (int(imageWidth * scale), int(imageHeight * scale)))
        self.frameWidth = width
        self.frameHeight = height
        self.rect = Rect(0,0,width,height)
        self.columns = columns
        # try to auto-calculate total frames
        rect = self.masterImage.get_rect()
        self.lastFrame = (rect.width // width) * (rect.height // height) - 1

    def update(self, currentTime, rate = 0):

        if currentTime > self.lastTime + rate:
            self.frame += 1
            if self.frame > self.lastFrame:
                self.frame = self.firstFrame
            self.lastTime = currentTime
        # build current frame only if it changed
        if self.frame != self.oldFrame:
            frameX = (self.frame % self.columns) * self.frameWidth
            frameY = (self.frame // self.columns) * self.frameHeight
            rect = (frameX, frameY, self.frameWidth, self.frameHeight)
            self.image = self.masterImage.subsurface(rect)
            self.oldFrame = self.frame


    #position property
    def getpos(self): return self.rect.topleft
    def setpos(self,pos): self.rect.topleft = pos
    position = property(getpos,setpos)
    def __str__(self):
        return str(self.frame) + "," + str(self.firstFrame) + \
               "," + str(self.lastFrame)


def showText(font, x, y, text, color=(255, 255, 255)):
    imgText = font.render(text, True, color)
    screen.blit(imgText, (x, y))

# initialize pygame
pygame.init()
screen = pygame.display.set_mode((800, 400))

pygame.display.set_caption("Sprite动画演示")
font = pygame.font.Font(None, 25)
framerate = pygame.time.Clock()

group1 = pygame.sprite.Group()
group2 = pygame.sprite.Group()
for i in range(1,12):
    scale = 0.2 * i
    player = MySprite(screen)
    player.load("man.png", 50 , 64 , 8,scale)
    player.firstFrame = 0
    player.lastFrame = 7
    player.position = 50+5 * i * i, 50
    group1.add(player)

    player = MySprite(screen)
    player.load("dragon.png",  260, 150 , 3,1)
    player.position = 10+5 * i, 200
    group2.add(player)



# main loop
while True:
    framerate.tick(100)
    ticks= pygame.time.get_ticks()


    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    key = pygame.key.get_pressed()
    if key[pygame.K_ESCAPE]: sys.exit()

    screen.fill((0, 0, 100))
    group1.update(ticks, 60)
    group2.update(ticks,100)
    group1.draw(screen)
    group2.draw(screen)



    showText(font, 10, 10, "Sprite: " + str(player))

    pygame.display.update()




