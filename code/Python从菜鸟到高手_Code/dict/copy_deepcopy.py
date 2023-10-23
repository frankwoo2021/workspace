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

persons1= {"Name":"Bill", "age":30, "fullName":["Bill", "Gates"]}
persons2 = persons1.copy()

print("persons1",persons1)
print("persons2",persons2)
print("-------浅层复制---------")
print("-------修改第一层元素---------")
persons2['age'] = 54
print("persons1",persons1)
print("persons2",persons2)
print("-------修改第二层元素---------")
persons2["fullName"][1] = "Clinton"
print("persons1",persons1)
print("persons2",persons2)
print("-------深层复制---------")
from copy import deepcopy
persons1= {"Name":"Bill", "age":30, "fullName":["Bill", "Gates"]}
persons2 = persons1.copy()
persons3 = deepcopy(persons1)

persons1["fullName"][1] = "Clinton"
print("persons1", persons1)
print("persons2", persons2)
print("persons3", persons3)


