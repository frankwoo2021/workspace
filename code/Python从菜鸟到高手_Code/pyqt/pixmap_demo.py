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

from PyQt6.QtWidgets import (QWidget, QHBoxLayout,
    QLabel, QApplication)
from PyQt6.QtGui import QPixmap
import sys

class Pixmap(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):      

        hbox = QHBoxLayout(self)
        pixmap = QPixmap("face.png")

        lbl = QLabel(self)
        lbl.setPixmap(pixmap)

        hbox.addWidget(lbl)
        self.setLayout(hbox)
        self.move(300, 200)
        self.setWindowTitle('显示图像（QPixmap控件）')
        self.show()        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Pixmap()
    sys.exit(app.exec())