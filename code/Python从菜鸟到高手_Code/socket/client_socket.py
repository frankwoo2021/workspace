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
# 客户端Socket
host = 'localhost'
port = 9876
bufferSize = 1024
addr = (host,port)
tcpClientSocket = socket(AF_INET, SOCK_STREAM)
tcpClientSocket.connect(addr)
while True:
    data = input('>')
    if not data:
        break
    data = data.encode('utf-8')
    tcpClientSocket.send(data)
    data = tcpClientSocket.recv(bufferSize)
    print(data.decode('utf-8'))
tcpClientSocket.close()