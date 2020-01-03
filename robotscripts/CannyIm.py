# -*- coding: cp936 -*-
import sys
import numpy as np
import cv2
import KmeanToIm

#Im=cv2.imread('d:\\robots\\robotscripts\\data\\road1.jpg',0)
Im=cv2.imread('d:\\dress\\768x847.jpg',0)
##print Im.dtype
print str(type(Im))
#�ı����ͼ���ȷ��С400x300dpi 4:3
resizeIm=cv2.resize(Im,(400,300),interpolation=cv2.INTER_LINEAR) 


##KmeanIm=KmeanToIm.doKmean('d:\\robots\\robotscripts\\data\\road.jpg')
GaussianIm=cv2.GaussianBlur(resizeIm,(3,3),4)


# ��ֵ������õ���ֵ��ͼ


#CANNY��Ե��ȡ
edges=cv2.Canny(GaussianIm,5,50, apertureSize = 3)

#HOUGH�任�õ�ֱ��
minLineLength = 1
maxLineGap = 1
lines = cv2.HoughLines(edges,1,np.pi/180,10)
##result = KmeanIm.copy()
result = resizeIm.copy()
lineps = cv2.HoughLinesP(edges,1,np.pi/180,10,minLineLength,maxLineGap)
for x1,y1,x2,y2 in lineps[0]:
	cv2.line(Im,(x1,y1),(x2,y2),(0,255,0),2)

#��ʾ���

#����任�����
result = resizeIm.copy()
for line in lines[0]:
	rho = line[0] #��һ��Ԫ���Ǿ���rho
	theta= line[1] #�ڶ���Ԫ���ǽǶ�theta
	print rho
	print theta
	if  (theta < (np.pi/4. )) or (theta > (3.*np.pi/4.0)): #��ֱֱ��
                #��ֱ�����һ�еĽ���
		pt1 = (int(rho/np.cos(theta)),0)
		#��ֱ�������һ�еĽ���
		pt2 = (int((rho-result.shape[0]*np.sin(theta))/np.cos(theta)),result.shape[0])
		#����һ������
		cv2.line( result, pt1, pt2, (255))
	else: #ˮƽֱ��
		# ��ֱ�����һ�еĽ���
		pt1 = (0,int(rho/np.sin(theta)))
		#��ֱ�������һ�еĽ���
		pt2 = (result.shape[1], int((rho-result.shape[1]*np.cos(theta))/np.sin(theta)))
		#����һ��ֱ��
		cv2.line(result, pt1, pt2, (255), 1)
cv2.namedWindow('Canny',flags=cv2.WINDOW_NORMAL)
cv2.imshow('orginIm',resizeIm)
cv2.imshow('Gaussian',GaussianIm)		
cv2.imshow('Canny', edges )
edges2=edges.copy()
edges2[200:400,:]=0
cv2.imshow('canny2',edges2)
cv2.imshow('Result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()

#������

cv2.imwrite('d:\\robots\\robotscripts\\data\\cannySave.jpg',edges)




