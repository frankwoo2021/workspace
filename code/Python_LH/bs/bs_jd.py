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

# 用Beautiful Soup分析京东首页的HTML代码

from bs4 import *
from urllib3 import *
disable_warnings()

http = PoolManager()
r = http.request('GET','https://www.jd.com')


soup = BeautifulSoup(r.data,'lxml')
print(soup.meta)
print(soup.meta['charset'])
print(soup.title.text)
print(soup.body['class'])