from PyQt6.QtGui import *
import random

'''给板块的一个Cell填色'''
def drawCell(painter, x, y, shape, blockSize):
    colors = [0xCC6666, 0x66CC66, 0x6666CC, 0xCCCC66, 0xCC66CC, 0x66CCCC, 0xDAAA00]
    if shape == 0:
        return
    color = QColor(colors[random.randint(0, 6)])
    painter.fillRect(int(x + 1), int(y + 1), int(blockSize - 2), int(blockSize - 2), color)
    painter.setPen(color.lighter())
    painter.drawLine(int(x), int(y + blockSize - 1), int(x),int(y))
    painter.drawLine(int(x), int(y), int(x + blockSize - 1), int(y))
    painter.setPen(color.darker())
    painter.drawLine(int(x + 1), int(y + blockSize - 1), int(x + blockSize - 1),int( y + blockSize - 1))
    painter.drawLine(int(x + blockSize - 1), int(y + blockSize - 1), int(x + blockSize - 1),int(y + 1))