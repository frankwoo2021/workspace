from .misc import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import QFrame

'''侧面板, 右边显示下一个俄罗斯方块的形状'''
class SidePanel(QFrame):
    def __init__(self, parent, blockSize, inner_board):
        super(SidePanel, self).__init__(parent)
        self.blockSize = blockSize
        self.inner_board = inner_board
        self.setFixedSize(blockSize * 5, blockSize * inner_board.height)
        self.move(blockSize * inner_board.width, 0)
    '''画侧面板'''
    def paintEvent(self, event):
        painter = QPainter(self)
        x_min, x_max, y_min, y_max = self.inner_board.next_tetris.getRelativeBoundary(0)
        dy = 3 * self.blockSize
        dx = (self.width() - (x_max - x_min) * self.blockSize) / 2
        shape = self.inner_board.next_tetris.shape
        for x, y in self.inner_board.next_tetris.getAbsoluteCoords(0, 0, -y_min):
            drawCell(painter, x * self.blockSize + dx, y * self.blockSize + dy, shape, self.blockSize)
    '''更新数据'''
    def updateData(self):
        self.update()