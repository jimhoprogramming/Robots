#-*- coding: utf8 -*-
import os
import stat
import struct

class JpegFlow(object):
    MAX_PACK_SIZE = 100
    SomeTime=0
    FileCounts=0
    FilesList=None
    FilePath=''
    def __init__(self,filePath=''):
        JpegFlow.FilePath=filePath
        JpegFlow.FileCount,JpegFlow.FilesList=self.ReadPathJpegFiles(filePath)
    def Start(self):
        if JpegFlow.SomeTime<=JpegFlow.FileCounts:
           JpegFlow.SomeTime+=1
        else:
           JpegFlow.SomeTime=0
        filename=JpegFlow.FilePath+'\\'+JpegFlow.FilesList[JpegFlow.SomeTime]   
        filesize = os.stat(filename)[stat.ST_SIZE]  #获得系统中某个文件的字节数
        f = open(filename, "rb")                    #二进制文件的读取
        chList = []
        for i in range(0, filesize):
            (ch,) = struct.unpack("B", f.read(1))   #python中对码流的操作：struct.pack 和 struct.unpack的使用
            chList.append(ch)   
        return chList,filesize
    def ReadPathJpegFiles(self,path): 
        i = 0
        li=[]
        for f in os.listdir(path): 
            a,b = os.path.splitext(f) 
            #print(str(i))
            #print(a)
            #print(b)
            #print(os.sep)
            if b == '.jpg':
                li.append(f)
                #os.rename(f, str(i) + os.extsep+'dat') 
                i+=1
        return i,li


##if __name__=='__main__':
##    myJpegFlow=JpegFlow('d:\\Robots\\robotscripts\\data\\ground\\')
##    print myJpegFlow.ReadPathJpegFiles('d:\\Robots\\robotscripts\\data\\ground')
##    
