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
result = re.sub('Bill', 'Mike', 'Bill is my son')
print(result)

result = re.subn('Bill', 'Mike', 'Bill is my son，I like Bill')
print(result)
print(result[0])
print('替换总数','=',result[1])

result = re.sub('([0-9])([a-z]+)', r'产品编码（\1-\2)','01-1abc,02-2xyz,03-9hgf')
print(result)

def fun():
    return r'产品编码（\1-\2)'
result = re.subn('([0-9])([a-z]+)', fun(),'01-1abc,02-2xyz,03-9hgf')
print(result)
print(result[0])
print('替换总数','=',result[1])