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

import re
f = open('words.txt','r')
words = f.read()
wordList = re.split('[ ,;]+', words)
countDict = {}
for word in wordList:
    if countDict.get(word) == None:
        countDict[word] = 1
    else:
        countDict[word] = int(countDict[word]) + 1
for (key,value) in countDict.items():
    print(key,'=',value)
f.close()