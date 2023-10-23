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

spaceNum = 5				# 表示每一行星号一侧最多的空格数，本例是5
i = 1
lineSpaceNum =spaceNum   	# 表示当前行的前后空格数
triangle = []            		# 二维列表
# 开始生成三角形
while lineSpaceNum >= 0:
    # 生成星号左侧空格序列
    leftSpaceList = [' '] * lineSpaceNum
    # 生成星号列表
    starList = ['*'] * (2 * i - 1)
    # 生成星号右侧空格序列
    rightSpaceList = [' '] * lineSpaceNum
    # 生成每一行的序列
    lineList = leftSpaceList + starList + rightSpaceList
    triangle.append(lineList)
    lineSpaceNum -= 1
    i += 1
for line in triangle:
    print(line)
