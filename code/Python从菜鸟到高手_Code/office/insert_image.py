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

from openpyxl import Workbook
wb = Workbook()
ws = wb.active
ws.title = '插入图像'


from openpyxl.drawing.image import Image

image = Image('book.png')
new_size = (200,200)
image.width,image.height = new_size
ws.add_image(image,'B3')
wb.save('images.xlsx')
