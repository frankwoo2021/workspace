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

import sys
sys.path.append('./test')

import my
my.greet('Bill')
#print(sys.modules)
print(sys.modules['my'])
print(type(sys.modules['my']))
print(sys.platform)

print(sys.argv[0])

if len(sys.argv) == 2:
    print(sys.argv[1])
    my.greet(sys.argv[1])

s = sys.stdin.read(6)
print(s)
sys.stdout.writelines('hello world')
print()
sys.stderr.writelines('error')

sys.exit(123)



