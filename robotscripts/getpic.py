# -*- coding: cp936 -*-
'''
Created on 2016-10-29

@author: Administrator
'''
import cv2
import sys,time
# print sys.path


class pic:
    def __init__(self,SavePath='',SaveName=''):
        #��ʼ���õ��ı�������
        self.FileName=SavePath+'\\'+SaveName+'.jpg'
    def snapshot(self): 
        print 'this is get picture program .'  
        print cv2.__version__
        #ȡ������ͷӲ���豸
        capture=cv2.VideoCapture(0)
        size = (int(capture.get(cv2.CAP_PROP_FRAME_WIDTH)),int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
        print size
        
        #video=cv2.VideoWriter("VideoTest.avi",cv2.VideoWriter_fourcc('P','I','M','1'), 0.3, size,1)
        if capture.isOpened():
            print('camera is open')
        else:
            print('camera not ready')
            exit            
        num=0
        while True:
            ret,img=capture.read()
            #��Ƶ�е�ͼƬһ����д��
            #video.write(img)
            #cv2.imshow('camera show',img)
            key=cv2.waitKey(2)
            cv2.imwrite(str(self.FileName),img)
            num=num+1
            if key==ord('q'):#ordΪ���������Ӧ������,
                break
#             if key==ord('s'):#ordΪ���������Ӧ������,
#                 time.sleep(10)
#                 ret,img=capture.read()
#                 key=cv2.waitKey(30)
#                 cv2.imshow('get show',img)
# 
#                 print(u'������Ƭ��ɡ�')
#                 break
            if num==5:
                break
            #print('capture again')       
        #cv2.destroyAllWindows()
        return img 
    def cleanPic(self):
        pass
        
        
        
        
if __name__ == '__main__':
    mypic=pic('.','FrontBody')
    mypic.snapshot()
             
