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

from bs4 import *
from urllib3 import *
disable_warnings()

http = PoolManager()
r = http.request('GET', 'https://www.taobao.com')
soup = BeautifulSoup(r.data, 'lxml')
navitems_group = soup.find_all('ul',class_='nav-bd')  # hd同样的
for tag in navitems_group[0].contents:    
    if tag.name == 'li' and tag.get('class') == None:
        print(tag.text)

def filter(tag):
    if tag.name == 'li'  and tag.parent.name == 'ul' and \
        tag.parent.get('class') == ['nav-hd']:
        return True
    return False
    
tags = soup.find_all(filter)
for tag in tags:
    print(tag.text)
