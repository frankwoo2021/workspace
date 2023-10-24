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

from socketserver import (TCPServer as TCP,StreamRequestHandler as SRH)
from time import ctime

host = ''
port = 9876
addr = (host,port)
class MyRequestHandler(SRH):
    def handle(self):
        print('客户端已经连接，地址：',self.client_address)
        self.wfile.write(ctime().encode(encoding='utf-8') + b' ' + self.rfile.readline())
print('正在等待客户端的连接')
tcpServer = TCP(addr, MyRequestHandler)
tcpServer.serve_forever()