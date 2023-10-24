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
pygame.display.set_caption("碰撞音效")
font = pygame.font.Font('simfang.ttf', 25)
timer = pygame.time.Clock()

group = pygame.sprite.Group()

spriteList = []
spriteColors = ['红圆', '绿圆', '蓝圆', '红块', '绿块', '蓝块', '鳄鱼']
spriteCollisionAudioFlags = {}
for i in range(0,3):
    spriteList.append(MySprite())
    spriteList[i].load(f"circle{i + 1}.png")
    spriteList[i].position = random.randint(10,700), random.randint(10,400)
    group.add(spriteList[i])
# create the player sprite
for i in range(3,6):
    spriteList.append(MySprite())
    spriteList[i].load(f"rect{i - 2}.png")
    spriteList[i].position = random.randint(10,700), random.randint(10,300)
    group.add(spriteList[i])
spriteList.append(MySprite())
spriteList[len(spriteList) - 1].load('cayman.png')
spriteList[len(spriteList) - 1].position = random.randint(10,700), random.randint(10,300)

group.add(spriteList[len(spriteList) - 1])

def playSound(sound, volume = 1):
    channel = pygame.mixer.find_channel(True)
    channel.set_volume(volume)
    channel.play(sound)

def verifyCollision():
    collisionState = ''
    xIndex = 0
    for i in range(0, len(spriteList)):
        for j in range(i + 1, len(spriteList)):
            result = pygame.sprite.collide_mask(spriteList[i], spriteList[j])
            key = spriteColors[i] + spriteColors[j]
            if result:
                collisionState = f'<{spriteColors[i]}>与<{spriteColors[j]}>碰撞'
                showText(font, 10, 10 + xIndex * 30, collisionState)

                if spriteCollisionAudioFlags.get(key) == None or spriteCollisionAudioFlags.get(key) == False:
                    playSound(sound, 0.5)
                    spriteCollisionAudioFlags[key] = True
                xIndex += 1
            else:
                spriteCollisionAudioFlags[key] = False

bgSound = pygame.mixer.Sound("bg.ogg")
sound = pygame.mixer.Sound("sound.wav")

playSound(bgSound, 0.1)
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
    group.update()
    group.draw(screen)
    verifyCollision()
    pygame.display.update()


