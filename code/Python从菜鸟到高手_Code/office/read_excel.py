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

wb = openpyxl.load_workbook('first.xlsx',data_only=True)
print(type(wb))

print('获取所有工作表的名字')
print(wb.sheetnames,'\n')

for sheet in wb:
    print(sheet.title)

sheet = wb['新的Sheet3']
print(type(sheet))

print(sheet.title)
print(sheet.sheet_properties.tabColor.rgb)
print(sheet['E6'].value)
wb.close()


