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

from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
import os
import sys
# 导入自定义模块
from libs import *
class Tetris(QMainWindow):
    def __init__(self, parent=None):
        super(Tetris, self).__init__(parent)

        self.initUI()
    # 初始化游戏界面
    def initUI(self):
        # 设置游戏图标
        self.setWindowIcon(QIcon(os.path.join(os.getcwd(), 'images/icon.png')))
        self.setWindowTitle('俄罗斯方块')
        self.blockSize = 25
        self.gameController = GameController()
        self.gameBoard = GameBoard(self, self.blockSize, self.gameController)


        self.setFixedSize(self.gameBoard.width() ,
                          self.gameBoard.height() )
        self.show()
        self.center()

    # 让游戏窗口居中
    def center(self):
        screen = QGuiApplication.primaryScreen().availableGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) // 2, (screen.height() - size.height()) // 2)
'''run'''
if __name__ == '__main__':
    app = QApplication([])
    tetris = Tetris()
    sys.exit(app.exec())