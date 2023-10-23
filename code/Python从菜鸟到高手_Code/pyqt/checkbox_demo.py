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

from PyQt6.QtWidgets import QWidget, QCheckBox, QApplication
from PyQt6.QtCore import Qt
import sys

class CheckBox(QWidget):
    
    def __init__(self):
        super().__init__()        
        self.initUI()
        
    def initUI(self):      

        cb = QCheckBox('请选择我', self)
        cb.move(20, 20)
        #cb.toggle()
        cb.stateChanged.connect(self.changeTitle)
        
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('还没有选择我')
        self.show()
        
        
    def changeTitle(self, state):
        if state == 2:
            self.setWindowTitle('已经选择我了')
        else:
            self.setWindowTitle('还没有选择我')

            
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CheckBox()
    sys.exit(app.exec())