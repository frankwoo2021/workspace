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
f = open('./files/urls.txt','r+')
url = ''
while True:
    url = f.readline()
    url = url.rstrip()
    if url == '':
        break;
    else:
        print(url)
print('-----------')
f.seek(0)
print(f.readlines())

f.write('https://jiketiku.com' + os.linesep)
f.close()

f = open('./files/urls.txt','a+')
urlList = ['https://geekori.com' + os.linesep, 'https://www.google.com' + os.linesep]
f.writelines(urlList)
f.close()