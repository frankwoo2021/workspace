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
from PyQt6.QtWidgets import QWidget, QLabel, QApplication

class AbsoluteLayout(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        lbl1 = QLabel('姓名', self)
        lbl1.move(15, 10)

        lbl2 = QLabel('年龄', self)
        lbl2.move(35, 40)

        lbl3 = QLabel('所在城市', self)
        lbl3.move(55, 70)        

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('绝对布局')    
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = AbsoluteLayout()
    sys.exit(app.exec())