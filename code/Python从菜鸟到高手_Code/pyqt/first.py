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
# PyQT6 ，QT6
import sys
from PyQt6.QtWidgets import QApplication, QWidget
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(450, 260)
    w.move(300, 300)
    w.setWindowTitle('第一个PyQt6应用')
    w.show()
    sys.exit(app.exec())