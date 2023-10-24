#########################################################################
# 作者:李宁（蒙娜丽宁）
#
# 微信公众号：极客起源
#
# B站：https://space.bilibili.com/477001733
#
# Copyright © 2022 Lining. All rights reserved.
#
# 版本: 2.0
#########################################################################

from PyQt6.QtWidgets import (QWidget, QLabel,
    QComboBox, QApplication)
from PyQt6.QtCore import pyqtBoundSignal
import sys

class ComboBox(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):      

        self.lbl = QLabel("中国", self)
        self.lbl.move(50, 150) 
        combo = QComboBox(self)
        combo.addItem("中国")
        combo.addItem("美国")
        combo.addItem("法国")
        combo.addItem("德国")
        combo.addItem("俄罗斯")
        combo.addItem("澳大利亚")
        combo.move(50, 50)
        self.lbl.move(50, 150)

        combo.currentTextChanged[str].connect(self.onCurrentTextChanged)

        combo1 = QComboBox(self)
        combo1.addItem("Item1")
        combo1.addItem("Item2")
        combo1.addItem("Item3")
        combo1.move(200, 50)
 
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('QComboBox控件')
        self.show()
        
        
    def onCurrentTextChanged(self, text):
      
        self.lbl.setText(text)
        self.lbl.adjustSize()  
        
                
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = ComboBox()
    sys.exit(app.exec())