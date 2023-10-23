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
result = re.split(';','Bill;Mike;John')
print(result)
result = re.split('[,;.\s]+','a,b,,d,d;x    c;d.  e')
print(result)
result = re.split('[a-z]{3}-[0-9]{2}','testabc-4312productxyz-43abill')
print(result)

result = re.split('[a-z]{3}-[0-9]{2}','testabc-4312productxyz-43abill',maxsplit=1)
print(result)