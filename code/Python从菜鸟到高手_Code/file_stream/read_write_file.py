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


f = open('./files/test1.txt','w')

print(f.write('I love '))
print(f.write('python'))
f.close()

f = open('./files/test1.txt', 'r')
print(f.read(7))
print(f.read(6))
f.close()
try:
    f = open('./files/test2.txt','r+')
except Exception as e:
    print(e)
f = open('./files/test2.txt', 'a+')
print(f.write('hello'))
f.close()

f = open('./files/test2.txt', 'a+')
print(f.read())
f.seek(0)
print(f.read())
f.close()
try:
    f = open('./files/test2.txt', 'w+')
    print(f.read())
    f.write('How are you?')
    f.seek(0)
    print(f.read())
finally:
    f.close()