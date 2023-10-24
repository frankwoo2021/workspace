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

import docx
doc = docx.Document()
doc.add_picture('book.png', width=docx.shared.Inches(1.6),
                            height=docx.shared.Cm(4))
doc.save('image.docx')