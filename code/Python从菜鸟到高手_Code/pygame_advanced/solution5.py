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
pygame.display.set_caption("矩形碰撞检测")
font = pygame.font.Font('simfang.ttf', 25)
timer = pygame.time.Clock()

group = pygame.sprite.Group()

rectList = []
rectColors = ['红块', '绿块', '蓝块']
# create the player sprite
for i in range(0,3):
    rectList.append(MySprite())
    rectList[i].load(f"rect{i + 1}.png")
    rectList[i].position = random.randint(10,600), random.randint(50,300)
    group.add(rectList[i])
def verifyCollision():
    collisionState = ''
    xIndex = 0
    for i in range(0, len(rectList)):
        for j in range(i + 1, len(rectList)):
            result = pygame.sprite.collide_rect(rectList[i], rectList[j])
            if result:
                collisionState = f'<{rectColors[i]}>与<{rectColors[j]}>碰撞'
                showText(font, 10, 10 + xIndex * 30, collisionState)
                xIndex += 1

while True:
    timer.tick(30)
    ticks = pygame.time.get_ticks()
    for event in pygame.event.get():
        if event.type == QUIT: sys.exit()
    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        sys.exit()
    elif keys[K_UP]:
        for k in range(0, len(rectList)):
            if keys[49 + k]:
                rectList[k].Y -= 1
    elif keys[K_RIGHT]:
        for k in range(0, len(rectList)):
            if keys[49 + k]:
                rectList[k].X += 1
    elif keys[K_DOWN]:
        for k in range(0, len(rectList)):
            if keys[49 + k]:
                rectList[k].Y += 1
    elif keys[K_LEFT] :
        for k in range(0, len(rectList)):
            if keys[49 + k]:
                rectList[k].X -= 1
    screen.fill((50, 50, 100))
    group.update()
    group.draw(screen)
    verifyCollision()
    pygame.display.update()


