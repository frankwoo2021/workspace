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
print(f'height:{ws.row_dimensions[10].height}')
ws.row_dimensions[10].height = 38

for i in range(12,15):
    ws.row_dimensions[i].height = 40

# 改变列宽
print(ws.column_dimensions['A'].width)
#ws.column_dimensions['A'].width = 50
for col in 'ABCDEFG':
    ws.column_dimensions[col].width = 15

wb.save('table1.xlsx')
wb.close()