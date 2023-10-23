
import os
import sys
from lib import *

from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *


# 俄罗斯方块主类
class Tetris(QMainWindow):
    def __init__(self, parent=None):

        super(Tetris, self).__init__(parent)
        # 是否暂停游戏
        self.isPaused = False
        # 是否开始ing
        self.isStarted = False
        self.initUI()
    # 初始化游戏界面
    def initUI(self):
        # 设置游戏图标
        self.setWindowIcon(QIcon(os.path.join(os.getcwd(), 'images/icon.png')))
        # 每一个小块的尺寸
        self.blockSize = 25
        # 游戏帧率，每200毫秒刷新一次
        self.fps = 200
        # 创建定时器，用于定时刷新游戏
        self.timer = QBasicTimer()
        # 焦点
        #  self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        # 水平布局
        layout_horizontal = QHBoxLayout()
        self.gameBoard = GameBoard()
        self.externalBoard = ExternalBoard(self, self.blockSize, self.gameBoard)
      #  layout_horizontal.addWidget(self.externalBoard)
        self.sidePanel = SidePanel(self, self.blockSize, self.gameBoard)
     #   layout_horizontal.addWidget(self.sidePanel)
        self.statusBar = self.statusBar()
        self.externalBoard.scoreSignal[str].connect(self.statusBar.showMessage)
        self.start()
        self.center()
        self.setWindowTitle('俄罗斯方块')
        self.show()
        self.setFixedSize(self.externalBoard.width() + self.sidePanel.width(), self.sidePanel.height() + self.statusBar.height())
    '''游戏界面移动到屏幕中间'''
    def center(self):
        screen = QGuiApplication.primaryScreen().availableGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) // 2, (screen.height() - size.height()) // 2)
    '''更新界面'''
    def updateWindow(self):
        self.externalBoard.updateData()
        self.sidePanel.updateData()
        self.update()
    #开始游戏
    def start(self):
        if self.isStarted:
            return
        self.isStarted = True
        # 产生新的小方块（由4个小块组成）
        self.gameBoard.createNewTetris()
        self.timer.start(self.fps, self)
    '''暂停/不暂停'''
    def pause(self):
        if not self.isStarted:
            return
        self.isPaused = not self.isPaused
        if self.isPaused:
            self.timer.stop()
            self.externalBoard.score_signal.emit('Paused')
        else:
            self.timer.start(self.fps, self)
        self.updateWindow()
    '''计时器事件'''
    def timerEvent(self, event):
        if event.timerId() == self.timer.timerId():
            removed_lines = self.gameBoard.moveDown()
            self.externalBoard.score += removed_lines
            self.updateWindow()
        else:
            super(Tetris, self).timerEvent(event)
    '''按键事件'''
    def keyPressEvent(self, event):
        if not self.isStarted or self.gameBoard.currentGame == tetrisShape().shape_empty:
            super(Tetris, self).keyPressEvent(event)
            return
        key = event.key()
        # P键暂停
      
        if key == Qt.Key.Key_P:
            self.pause()
            return
        if self.isPaused:
            return
        # 向左
        elif key == Qt.Key.Key_Left:
            self.gameBoard.moveLeft()
        # 向右
        elif key == Qt.Key.Key_Right:
            self.gameBoard.moveRight()
        # 逆时针旋转
        elif key == Qt.Key.Key_Up:
            self.gameBoard.rotateAnticlockwise()
        elif key == Qt.Key.Key_Down:
            self.gameBoard.rotateClockwise()
        # 快速坠落
        elif key == Qt.Key.Key_Space:
            self.externalBoard.score += self.gameBoard.dropDown()
        else:
            super(Tetris, self).keyPressEvent(event)
        self.updateWindow()


'''run'''
if __name__ == '__main__':
    app = QApplication([])
    tetris = Tetris()
    sys.exit(app.exec())