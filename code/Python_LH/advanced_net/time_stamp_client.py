#########################################################################
# 作者:李宁（蒙娜丽宁）
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

host = 'localhost'
port = 9876
class MyProtocol(protocol.Protocol):
    def sendData(self):
        data = input('>')
        if data:
            print('...正在发送 %s' % data)
            self.transport.write(data.encode(encoding='utf_8'))
        else:
            self.transport.loseConnection()
    def connectionMade(self):
        self.sendData()
    def dataReceived(self,data):
        print(data.decode('utf-8'))
        self.sendData()
class MyFactory(protocol.ClientFactory):
    protocol = MyProtocol
    clientConnectionLost = clientConnectionFailed = lambda self,connector,reason:reactor.stop()
reactor.connectTCP(host,port,MyFactory())
reactor.run()