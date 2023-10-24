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
from PyQt6.QtWidgets import QWidget, QMessageBox, QApplication
class MessageBox(QWidget):
    def __init__(self):
        super().__init__()        
        self.initUI()
    def initUI(self):                       
        self.setGeometry(300, 300, 250, 150)        
        self.setWindowTitle('消息盒子') 
        self.show()
        
    def closeEvent(self, event):
        reply = QMessageBox.question(self, '消息',
            "你真的要退出吗?",  QMessageBox.StandardButton.Yes |
                                     QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = MessageBox()
    sys.exit(app.exec())
