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
print(type(doc))
p = doc.add_paragraph('Hello, world!')
p.runs[0].underline = True
p.runs[0].italic = True
doc.save('helloworld.docx')