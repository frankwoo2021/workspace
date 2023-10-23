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
from PyQt6.QtWidgets import (QWidget, QLabel,
    QLineEdit, QApplication)


class LineEdit(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):      

        self.label = QLabel(self)
        lineEdit = QLineEdit(self)        
        lineEdit.move(80, 100)
        self.label.move(80, 40)

        lineEdit.textChanged[str].connect(self.onChanged)
        
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('QLineEdit控件')
        self.show()
        
        
    def onChanged(self, text):
        
        self.label.setText(text)
        self.label.adjustSize()        
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = LineEdit()
    sys.exit(app.exec())