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

import os
import subprocess
print(os.sep)
print(os.pathsep)
print(os.name)

print(os.environ)
print(os.environ['PATH'])
print(os.getenv('PATH'))
output = subprocess.getstatusoutput('exe')
print(output)
os.putenv('PATH', os.getenv('PATH') + os.pathsep+ '/temp/exe')


output = subprocess.getstatusoutput('exe')
print(output)
print(os.getenv('PATH'))

os.system('ls -al')

