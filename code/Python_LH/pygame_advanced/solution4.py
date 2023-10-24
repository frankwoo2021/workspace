#########################################################################
# 作者:李宁（蒙娜丽宁）
#
# 微信公众号：极客起源
#
# B站：https://space.bilibili.com/477001733
#
# Copyright © 2022 Lining. All rights reserved.
#
# 版本: 2.0
#########################################################################


import sys,  random,  pygame
from pygame.locals import *

class MySprite(pygame.sprite.Sprite):
    def __init__(self, target):
        pygame.sprite.Sprite.__init__(self) #extend the base Sprite class
        self.masterImage = None
        self.frame = 0
        self.oldFrame = -1
        self.firstFrame = 0
        self.lastFrame = 0
        self.columns = 1
        self.lastTime = 0

    #X property
    def getx(self): return self.rect.x
    def setx(self,value): self.rect.x = value
    X = property(getx,setx)

    #Y property
    def gety(self): return self.rect.y
    def sety(self,value): self.rect.y = value
    Y = property(gety,sety)

    #position property
    def _getpos(self): return self.rect.topleft
    def _setpos(self,pos): self.rect.topleft = pos
    position = property(_getpos,_setpos)

    def load(self, filename, width, height, columns):
        self.masterImage = pygame.image.load(filename).convert_alpha()
        self.frameWidth = width
        self.frameHeight = height
        self.rect = Rect(0,0,width,height)
        self.columns = columns
        #try to auto-calculate total frames
        rect = self.masterImage.get_rect()
        self.lastFrame = (rect.width // width) * (rect.height // height) - 1

    def update(self, currentTime,rate = 0):
        #update animation frame number
        if currentTime > self.lastTime + rate:
            self.frame += 1
            if self.frame > self.lastFrame:
                self.frame = self.firstFrame
            self.lastTime = currentTime

        #build current frame only if it changed
        if self.frame != self.oldFrame:
            frameX = (self.frame % self.columns) * self.frameWidth
            frameY = (self.frame // self.columns) * self.frameHeight
            rect = Rect(frameX, frameY, self.frameWidth, self.frameHeight)
            self.image = self.masterImage.subsurface(rect)
            self.oldFrame = self.frame

def resetFlame():
    y = random.randint(250,350)
    flame.position = 800,y
#main program begins
pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Sprite交互演示（按空格键弹跳）")
font = pygame.font.Font(None, 18)
framerate = pygame.time.Clock()

#load bitmaps
bg = pygame.image.load("background.png").convert_alpha()

group1 = pygame.sprite.Group()
group2 = pygame.sprite.Group()

#create the player sprite
player = MySprite(screen)
player.load("man.png", 50, 64, 8)
player.firstFrame = 1
player.lastFrame = 7
player.position = 400, 303
group1.add(player)

#create the Flame sprite
flame = MySprite(screen)
flame.load("flame.png", 40, 16, 1)
flame.position = 800,320
group2.add(flame)

flameVel = 8.0

playerJumping = False
jumpVel = 0.0
playerStartY = player.Y

#repeating loop
while True:
    framerate.tick(60)
    ticks = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == QUIT: sys.exit()
    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]: sys.exit()
    elif keys[K_SPACE]:
        if not playerJumping:
            playerJumping = True
            jumpVel = -14.0


    flame.X -= flameVel
    if flame.X < -40: resetFlame()


    #is the player jumping?
    if playerJumping:
        player.Y += jumpVel
        jumpVel += 0.5
        if player.Y > playerStartY:
            playerJumping = False
            player.Y = playerStartY
            jumpVel = 0.0


    #draw the background
    screen.blit(bg, (0,0))


    group1.update(ticks,60)

    #draw sprites
    group1.draw(screen)
    group2.update(ticks)

    #draw sprites
    group2.draw(screen)
    pygame.display.update()
