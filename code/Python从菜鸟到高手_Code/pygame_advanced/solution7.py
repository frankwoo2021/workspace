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

from GameLibrary import *

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("精灵与组之间的碰撞检测")
font = pygame.font.Font('simfang.ttf', 25)
timer = pygame.time.Clock()

group = pygame.sprite.Group()

spriteList = []
spriteColors = ['红圆', '绿圆', '蓝圆', '红块', '绿块', '蓝块']
for i in range(0,3):
    spriteList.append(MySprite())
    spriteList[i].load(f"circle{i + 1}.png")
    spriteList[i].name = spriteColors[i]
    spriteList[i].position = random.randint(10,700), random.randint(10,400)
    group.add(spriteList[i])
# create the player sprite
for i in range(3,6):
    spriteList.append(MySprite())
    spriteList[i].load(f"rect{i - 2}.png")
    spriteList[i].position = random.randint(10,700), random.randint(10,300)
    spriteList[i].name = spriteColors[i]
    group.add(spriteList[i])

walker = MySprite()
spriteList.append(walker)
walker.load('walker.png',8, 96, 96)

walker.position = random.randint(10,700), random.randint(10,300)

playerGroup = pygame.sprite.Group()
playerGroup.add(walker)
def callback(sprite1, sprite2):
    return pygame.sprite.collide_mask(sprite1, sprite2)
def verifyCollision():
    collideSpriteList = pygame.sprite.spritecollide(walker,group,False,callback)
    for i in range(0, len(collideSpriteList)):
        showText(font, 10, 10 + i * 30, f'<漫步者>与<{collideSpriteList[i].name}>碰撞')
while True:
    timer.tick(30)
    ticks = pygame.time.get_ticks()
    for event in pygame.event.get():
        if event.type == QUIT: sys.exit()
    keys = pygame.key.get_pressed()
    walkerTicks = 0

    if keys[K_ESCAPE]:
        sys.exit()
    elif keys[K_UP]:
        for k in range(0, len(spriteList)):
            if keys[49 + k]:
                spriteList[k].Y -= 1
                if k == 6:  # walker
                    walkerTicks = ticks
                    if walker.frame < walker.firstFrame or walker.frame > walker.lastFrame:
                        walker.frame = 0
                    walker.firstFrame = 0
                    walker.lastFrame = 7

    elif keys[K_RIGHT]:
        for k in range(0, len(spriteList)):
            if keys[49 + k]:
                spriteList[k].X += 1
                if k == 6:  # walker
                    walkerTicks = ticks
                    if walker.frame < walker.firstFrame or walker.frame > walker.lastFrame:
                        walker.frame = 16
                    walker.firstFrame = 16
                    walker.lastFrame = 23
    elif keys[K_DOWN]:
        for k in range(0, len(spriteList)):
            if keys[49 + k]:
                spriteList[k].Y += 1
                if k == 6:  # walker
                    walkerTicks = ticks
                    if walker.frame < walker.firstFrame or walker.frame > walker.lastFrame:
                        walker.frame = 32
                    walker.firstFrame = 32
                    walker.lastFrame = 39
    elif keys[K_LEFT] :
        for k in range(0, len(spriteList)):
            if keys[49 + k]:
                spriteList[k].X -= 1
                if k == 6:  # walker
                    walkerTicks = ticks
                    if walker.frame < walker.firstFrame or walker.frame > walker.lastFrame:
                        walker.frame = 48
                    walker.firstFrame = 48
                    walker.lastFrame = 55
    screen.fill((50, 50, 100))
    group.update()
    group.draw(screen)
    playerGroup.update(walkerTicks,50)
    playerGroup.draw(screen)
    verifyCollision()
    pygame.display.update()
