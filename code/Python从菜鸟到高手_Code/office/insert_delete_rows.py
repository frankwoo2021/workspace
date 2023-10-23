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

import openpyxl

wb = openpyxl.load_workbook('table1.xlsx')

ws = wb.active
# 在第一行前面插入一行
ws.insert_rows(1)

# 在第一行前面插入一行
ws.insert_rows(1)
# 在第一行前面插入多行

for i in range(5):
    ws.insert_rows(1)

ws.insert_rows(1,5)

# 在任意位置插入多行
ws.insert_rows(25,9)

# 删除行
ws.delete_rows(28,2)
wb.save('table1.xlsx')
wb.close()
