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
# 游戏控制器
class GameController:
    def __init__(self, width=12, height=28):
        self.width = width
        self.height = height

'''游戏面板'''
class GameBoard(QFrame):
    def __init__(self, parent, blockSize, gameBoard):
        super(GameBoard, self).__init__(parent)
        self.blockSize = blockSize
        self.gameBoard = gameBoard
        self.setFixedSize(blockSize * gameBoard.width, blockSize * gameBoard.height)
