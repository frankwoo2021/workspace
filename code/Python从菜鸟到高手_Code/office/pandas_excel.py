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

'''
1. Pandas（数据分析）
2. Numpy（科学计算）
3. Matplotlib（数据可视化）

1. Pandas如何读取Excel数据
2. 处理数据
3. 通过openpyxl想处理完的数据回写到Excel文件
'''

import pandas as pd

df = pd.read_excel('members.xlsx',sheet_name='marvel')
#print(df.head())  # 输出前5行

# 读取第1行数据
print(df.iloc[0])
print('-----')
# 读取第2行数据
print(df.iloc[1])

print(df[1:2])   # 显示第2行
print(df[1:2].values)
print(df[1:2].values[0])

# 读取第1行第2列
print(df.iloc[0][1])

# 将Excel数据转换为二维列表
marvel_data = []
print(df.index.values)
for i in df.index.values:
    marvel_data.append(df[i:i+1].values[0].tolist())
print(marvel_data)
# DataFrame = Sheet
# 列表
print('list-->',df.to_dict(orient='list'))
# 索引对象
print('index-->:',df.to_dict(orient='index'))

# 对象列表
print('records-->',df.to_dict(orient='records'))

# 字典
print('dict-->',df.to_dict(orient='dict'))

# 分拆数据
print('dict-->', df.to_dict(orient='split'))

from openpyxl import Workbook
wb = Workbook()

ws = wb.active

ws.sheet_properties.tabColor='FF0000'
ws.title = 'new_marvel'

for row in range(len(marvel_data)):
    for col in range(len(marvel_data[row])):
        if col == len(marvel_data[row]) - 1:
            marvel_data[row][col] += 50
        ws.cell(row + 1,col + 1, marvel_data[row][col])
wb.save('marvel.xlsx')
wb.close()






