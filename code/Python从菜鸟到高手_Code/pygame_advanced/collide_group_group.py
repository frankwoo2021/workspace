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
pygame.display.set_caption("组与组之间的碰撞检测")
font = pygame.font.Font('simfang.ttf', 25)
timer = pygame.time.Clock()

group1 = pygame.sprite.Group()
group2 = pygame.sprite.Group()
spriteList = []
spriteColors = ['红圆', '绿圆', '蓝圆', '红块', '绿块', '蓝块']
for i in range(0,3):
    spriteList.append(MySprite())
    spriteList[i].load(f"circle{i + 1}.png")
    spriteList[i].name = spriteColors[i]
    spriteList[i].position = random.randint(10,700), random.randint(10,400)
    group1.add(spriteList[i])
# create the player sprite
for i in range(3,6):
    spriteList.append(MySprite())
    spriteList[i].load(f"rect{i - 2}.png")
    spriteList[i].name = spriteColors[i]
    spriteList[i].position = random.randint(10,700), random.randint(10,300)
    group2.add(spriteList[i])
def callback(sprite1, sprite2):
    return pygame.sprite.collide_mask(sprite1, sprite2)
def verifyCollision():
    collideDict = pygame.sprite.groupcollide(group1, group2, False, False, callback)
    i = 0
    for k, v in collideDict.items():
        for sprite in v:
            showText(font, 10, 10 + i * 30, f'<{k.name}>与<{sprite.name}>发生了碰撞')
            i += 1
while True:
    timer.tick(30)
    ticks = pygame.time.get_ticks()
    for event in pygame.event.get():
        if event.type == QUIT: sys.exit()
    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        sys.exit()
    elif keys[K_UP]:
        for k in range(0, len(spriteList)):
            if keys[49 + k]:
                spriteList[k].Y -= 1
    elif keys[K_RIGHT]:
        for k in range(0, len(spriteList)):
            if keys[49 + k]:
                spriteList[k].X += 1
    elif keys[K_DOWN]:
        for k in range(0, len(spriteList)):
            if keys[49 + k]:
                spriteList[k].Y += 1
    elif keys[K_LEFT] :
        for k in range(0, len(spriteList)):
            if keys[49 + k]:
                spriteList[k].X -= 1
    screen.fill((50, 50, 100))
    group1.update()
    group1.draw(screen)
    group2.update()
    group2.draw(screen)
    verifyCollision()
    pygame.display.update()


