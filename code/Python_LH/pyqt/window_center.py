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
from PyQt6.QtWidgets import QWidget,QApplication
from PyQt6.QtGui import QGuiApplication

class CenterWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):               
        
        self.resize(250, 150)
        self.center()        
        self.setWindowTitle('窗口居中')    
        self.show()
    def center(self):
        screen = QGuiApplication.primaryScreen().availableGeometry()
        self.move(int((screen.width()- self.width())/2),int((screen.height()- self.height())/2))

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = CenterWindow()
    sys.exit(app.exec())