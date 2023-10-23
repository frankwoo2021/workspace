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
bufferSize = 1024
port = 9876
addr = (host,port)
tcpServerSocket = socket(AF_INET, SOCK_STREAM)
tcpServerSocket.bind(addr)
tcpServerSocket.listen(2)
print('Server port:9876')
print('正在等待客户端连接')
while True:
    tcpClientSocket,addr = tcpServerSocket.accept()
    print('客户端已经连接','addr','=',addr)
    data = tcpClientSocket.recv(bufferSize)
    print(data.decode('utf8'))
    tcpClientSocket.send('你好，I love you.\n'.encode(encoding='utf_8'))
    tcpClientSocket.close()

tcpServerSocket.close()
        
        