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

import sqlite3
import os

dbPath = 'data.sqlite'
if not os.path.exists(dbPath):
    conn = sqlite3.connect(dbPath)
    c = conn.cursor()
    c.execute('''CREATE TABLE persons
       (id INT PRIMARY KEY     NOT NULL,
       name           TEXT    NOT NULL,
       age            INT     NOT NULL)''')


    conn.commit()
    conn.close()
conn = sqlite3.connect(dbPath)
c = conn.cursor()
while True:
    id = input('请输入id：')
    if id == 'exit:':
        break;
    id = int(id)
    name = input('请输入name：')
    if name == 'exit:':
        break;
    age = input('请输入age：')
    if age == 'exit:':
        break;   
    age = int(age) 
    c.execute("INSERT INTO persons (id,name,age) \
          VALUES ({},'{}',{})".format(id,name,age));

conn.commit()


persons = c.execute("select id,name,age from persons order by age")

result = []
for person in persons:
    value = {}
    value['id'] = person[0]
    value['name'] = person[0]
    value['age'] = person[1]  
    result.append(value)
conn.close() 

print(result)




