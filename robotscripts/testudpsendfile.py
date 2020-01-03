#-*- coding: utf8 -*-
import socket
import os
import stat
import struct

MAX_PACK_SIZE = 100
DEST_IP = 'localhost'
DEST_PORT = 17800

filename = raw_input("input filename")

filesize = os.stat(filename)[stat.ST_SIZE]  #获得系统中某个文件的字节数

f = open(filename, "rb")                    #二进制文件的读取

chList = []
for i in range(0, filesize):
    (ch,) = struct.unpack("B", f.read(1))   #python中对码流的操作：struct.pack 和 struct.unpack的使用
    chList.append(ch)

client = socket.socket( socket.AF_INET, socket.SOCK_DGRAM )   #UDP客户端最简单的实现

packSize = 0
string = ""
args = []
for i in range(0, filesize):
    packSize = packSize + 1
    string = string + struct.pack("B", chList[i])
    if (MAX_PACK_SIZE == packSize or i == filesize - 1):
        client.sendto(string, (DEST_IP, DEST_PORT))
        packSize = 0
        string = ""
client.close()
