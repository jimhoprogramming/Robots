import cv2
import numpy as np

def getY():
    a=np.load('d:\\robots\\robotscripts\\a.npy')
    return a

def setY():
    a=np.array([(1,'ground','\d\\robots\\robotscripts\\data\\ground',1)],\
               dtype=[('TID','i4'),\
                      ('TName','S6'),\
                      ('SaveURL','S64'),\
                      ('showColor','i4')])
    np.save('d:\\robots\\robotscripts\\a', a)

def getXY(url='',size=[],YIDnum=1,saveTo=''):
    print 'url=%s , size=%2dX%2d ,YID=%4d,SaveTo=%s'%(url,size[0],size[1],YIDnum,saveTo)
    
