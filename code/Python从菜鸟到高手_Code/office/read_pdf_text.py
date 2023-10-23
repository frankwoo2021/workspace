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
import PyPDF2
pdfFileObj = open('pdf_filename.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
print('页数：',pdfReader.numPages)
pageObj = pdfReader.getPage(0)
print(pageObj.extractText())
pdfFileObj.close()