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
host = 'localhost'
port = 9999
bufferSize = 1024
addr = (host, port)
udpClientSocket = socket(AF_INET, SOCK_DGRAM)
while True:
    data = input('>')
    if not data:
        break
    udpClientSocket.sendto(data.encode(encoding='utf-8'),addr)
    data,addr = udpClientSocket.recvfrom(bufferSize)
    if not data:
        break
    print(data.decode('utf-8'))
udpClientSocket.close()
    
    