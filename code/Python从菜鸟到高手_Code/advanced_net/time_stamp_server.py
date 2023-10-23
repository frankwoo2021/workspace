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

from twisted.internet import protocol,reactor
from time import ctime
port = 9876
class MyProtocol(protocol.Protocol):
    def connectionMade(self):
        client = self.transport.getPeer().host
        print('客户端',client,'已经连接')
    def dataReceived(self,data):
        self.transport.write(ctime().encode(encoding='utf-8') + b' ' + data)
factory = protocol.Factory()
factory.protocol = MyProtocol
print('正在等待客户端连接')
reactor.listenTCP(port,factory)
reactor.run()
