#-*- coding: utf8 -*-
#名称：udpServer
#此程式目的:实现模拟"滚开"wifi的udp服务器替代功能。
#输入没
#输出为udp发送‘ok’
#使用WXPYTHON 自带的Socket库完成

import socket
import SendJpeg
import struct

if __name__ == "__main__":
    #初始化数据常量
    remoteHOST, remotePORT = "192.168.0.4", 10005
    sentdata = "ok"
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #定义socket类型，网络通信，TCP


    #作为客户端才去主动建立连接动作，服务器端不用这个行为
    #sock.connect((remoteHOST, remotePORT))

    #作为服务器负责监听外界有没要求建立连接动作。
    sock.bind((remoteHOST, remotePORT))                 #把监听绑定到具体地址和端口
    #sock.listen(1)                                     #开始TCP监听,udp不用监听步骤
    sock.settimeout(30)
    try:
        #while True:
        #    conn,addr=sock.accept()                    #接受TCP连接，并返回新的套接字与IP地址
            while True:
                #rcdata = conn.recv(1024)               #tcp把接收的数据实例化
                rcdata,addr=sock.recvfrom(32)            #udp直接接收数据
                if rcdata.__len__()>0:
                    #conn.sendall(sentdata + "\n")      #tcp要用传来的地址发数据
                    if rcdata=='cammera':
                        MAX_PACK_SIZE=1024
                        mySentJpeg=SendJpeg.JpegFlow('d:\\Robots\\robotscripts\\data\\ground')
                        chList,filesize=mySentJpeg.Start()
                        packSize = 0
                        string = ""
                        args = []
                        n=0
                        for i in range(0, filesize):
                            packSize = packSize + 1
                            string = string + struct.pack("B", chList[i])
                            if (MAX_PACK_SIZE == packSize or i == filesize - 1):
                                n=n+1
                                sock.sendto(string, addr)
                                packSize = 0
                                print(u'发送第%d段数据'%(n))
                                string = ""
                        print(u'图片文件发送完成。')
                    else:
                        sock.sendto(sentdata,addr)   #udp用回自己的套接字发送数据
                        print "Sent:     {}".format(sentdata)
                    print "Received: {}".format(rcdata)
                    
    except socket.timeout:
        print(u'等待终端激活信号超时，没有连接或没有接收到数据！')
