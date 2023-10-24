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


dict1 = {
    'title':'欧瑞学院',
    'website':'https://geekori.com',
    'description':'从事在线IT课程研发和销售'    
    }
dict2 = {
    'title':'欧瑞科技',
    'products':['欧瑞学院','博客','读书频道','极客题库','OriUnity'],
    'description':'从事在线IT课程研发和销售，工具软件研发'
    }
dict1.update(dict2)
for item in dict1.items():
    print("key = {key}  value = {value}".format(key = item[0],value = item[1]))
