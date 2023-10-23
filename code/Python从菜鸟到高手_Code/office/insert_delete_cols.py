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
# 在第一列前面插入一列
ws.insert_cols(1)
# 在第一列前面插入多列
ws.insert_cols(1,10)
# 在任意位置插入多列
ws.insert_cols(3,5)
# 删除列
ws.delete_cols(3,5)
wb.save('table1.xlsx')
wb.close()