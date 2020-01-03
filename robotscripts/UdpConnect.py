#-*- coding: utf8 -*-
#名称：UdpConnect
#此程式目的:实现连接"滚开"wifi的udp服务功能。
#输入为要发送的字符指令
#输出为udp服务器连通或中断的逻辑状态值
#使用WXPYTHON 自带的Socket库完成

import socket
#import ctypes

class UdpConnect(object):
    udpServerSocket=None
    bufferSize=1024
    # The remote host
    HOST = '192.168.0.4'
    # The same port as used by the server
    PORT = 10005            
    def __init__(self):
        UdpConnect.udpServerSocket= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)    
    def Connect(self):
        UdpConnect.udpServerSocket.connect((UdpConnect.HOST, UdpConnect.PORT))
    def SendCharter(self,sendData=' '):
        #发送数据指令
        UdpConnect.udpServerSocket.sendall(sendData)
        #检测返回值看是否成功送达
        UdpConnect.udpServerSocket.settimeout(1)
        receiveData=''
        receiveDataLen=0
        n=0
        try:
            while 1:
                n=n+1
                tempReceiveData,addc = self.udpServerSocket.recvfrom(UdpConnect.bufferSize)   
                receiveDataLen=receiveDataLen+tempReceiveData.__len__()
                receiveData=receiveData+tempReceiveData
                print(u'接收第 %d 的次数据。'%(n)) 
                if (tempReceiveData.__len__()<UdpConnect.bufferSize):
                    print(u'完成一次接收完整数据动作。') 
                    break
            print(u'返回数据 %d 字节数据'%(receiveDataLen))        
        except socket.timeout:
            print(u'滚开没有连接或没有返回数据！')
            return 0,0
        return receiveDataLen,receiveData
    def DisConnect(self):
        UdpConnect.udpServerSocket.close()
        print(u'滚开的连接被断开')
        
##myudp=UdpConnect()
##myudp.Connect()
##print myudp.SendCharter('L')
##myudp.DisConnect()
