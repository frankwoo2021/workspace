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

host = ''
bufferSize = 2
port = 9876
addr = (host,port)
tcpServerSocket = socket(AF_INET, SOCK_STREAM)
tcpServerSocket.bind(addr)
tcpServerSocket.listen()
print('Server port:9876')
print('正在等待客户端连接')
tcpClientSocket,addr = tcpServerSocket.accept()
print('客户端已经连接','addr','=',addr)
fullDataBytes = b''
while True:    
    data = tcpClientSocket.recv(bufferSize)
    fullDataBytes += data
    if len(data) < bufferSize:
        break;
print(fullDataBytes)
print(fullDataBytes.decode('ISO-8859-1'))
tcpClientSocket.close()
tcpServerSocket.close()
        
        