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
pygame.display.set_caption("圆形碰撞检测")
font = pygame.font.Font('simfang.ttf', 25)
timer = pygame.time.Clock()

group = pygame.sprite.Group()

circleList = []
circleColors = ['红圆', '绿圆', '蓝圆']
# create the player sprite
for i in range(0,3):
    circleList.append(MySprite())
    circleList[i].load(f"circle{i + 1}.png")
    circleList[i].position = random.randint(10,600), random.randint(50,300)
    group.add(circleList[i])
def verifyCollision():
    collisionState = ''
    xIndex = 0
    for i in range(0, len(circleList)):
        for j in range(i + 1, len(circleList)):
            result = pygame.sprite.collide_circle_ratio(0.8)(circleList[i], circleList[j])
            if result:
                collisionState = f'<{circleColors[i]}>与<{circleColors[j]}>碰撞'
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
        for k in range(0, len(circleList)):
            if keys[49 + k]:
                circleList[k].Y -= 1
    elif keys[K_RIGHT]:
        for k in range(0, len(circleList)):
            if keys[49 + k]:
                circleList[k].X += 1
    elif keys[K_DOWN]:
        for k in range(0, len(circleList)):
            if keys[49 + k]:
                circleList[k].Y += 1
    elif keys[K_LEFT] :
        for k in range(0, len(circleList)):
            if keys[49 + k]:
                circleList[k].X -= 1
    screen.fill((50, 50, 100))
    group.update()
    group.draw(screen)
    verifyCollision()
    pygame.display.update()


