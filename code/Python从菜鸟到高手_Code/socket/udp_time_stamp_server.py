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

from socket import *
from time import ctime
host = ''
port = 9876
bufferSize = 1024
addr = (host, port)
udpServerSocket = socket(AF_INET, SOCK_DGRAM)
udpServerSocket.bind(addr)
while True:
    print('正在等待消息......')
    data, addr = udpServerSocket.recvfrom(bufferSize)
    udpServerSocket.sendto(ctime().encode(encoding='utf-8') + b' ' + data,addr)
    print('客户端地址：',addr)
udpServerSocket.close()