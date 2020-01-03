# Echo client program
import socket 
#from struct import *
import ctypes 
import sys
#libc = cdll.msvcrt
#printf = libc.printf
print('program start........')
myfile=open('d:\\robots\\robotscripts\\data\\other.jpg','wb')


def udpget():
    HOST = '192.168.0.3'    # The remote host
    PORT = 10002           # The same port as used by the server
    bufsize=32
    udpServerSocket= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udpServerSocket.connect((HOST, PORT))
    udpServerSocket.sendall('123456')  #activeity arduno system server to send jpeg
    jpglen=0
    udpServerSocket.settimeout(12)
    try:
        while 1:
            data,addc = udpServerSocket.recvfrom(bufsize)   
    ##        print(data.__len__())
            jpglen=jpglen+data.__len__()
            savefile(data)
            if (data.__len__()<32): break
    ##        print(repr(data))      #output data but what type data?
        print('get jpg over!!have %d K bytes to save files'%(jpglen/1024))
    except socket.timeout:
        print('arduno system no respond! close file')
    udpServerSocket.close()
    myfile.close()
    

def savefile(dataLine32):
##    p=[ctypes.c_ubyte(0xff),ctypes.c_ubyte(0xd8),ctypes.c_ubyte(0x00),ctypes.c_ubyte(0x0d)]
##    type(data)    
    for c in dataLine32:
##        print(repr(c))
        myfile.write(c)

udpget()
