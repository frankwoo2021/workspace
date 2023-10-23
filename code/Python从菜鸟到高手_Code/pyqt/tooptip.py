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

import sys
from PyQt6.QtWidgets import (QWidget, QToolTip,
    QPushButton, QApplication)
from PyQt6.QtGui import QFont

        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QWidget()
    w.setGeometry(300, 300, 300, 220)
    w.setWindowTitle('提示框')    
    QToolTip.setFont(QFont('SansSerif', 20))        
    w.setToolTip('这是一个窗口\n设计者：李宁')
    btn = QPushButton('Button', w)
    btn.setToolTip('这是一个按钮\n设计者：Lining')
    btn.resize(btn.sizeHint())
    btn.move(50, 50)       
    w.show()
    sys.exit(app.exec())