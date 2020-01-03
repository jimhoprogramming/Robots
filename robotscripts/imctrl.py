# -*- coding: cp936 -*-
import sys
##import Image
##import ImageFilter
##from scipy import ndimage as ndi
##from skimage import feature
import numpy as np
##import matplotlib.pyplot as plt
import cv2 

#Im=Image.open('d:\\robots\\robotscripts\\data\\road.jpg')
##Im=ndi.imread('d:\\robots\\robotscripts\\data\\road.jpg',flatten=False,mode='L')
Im=cv2.imread('d:\\robots\\robotscripts\\data\\road.jpg',0)
##print Im.dtype




# Generate noisy image of a square
##Im = np.zeros((128, 128))
##Im[32:-32, 32:-32] = 1

##Im = ndi.rotate(Im, 15, mode='constant')
##Im = ndi.median_filter(Im, 3)
##Im = ndi.gaussian_filter(Im, 1)
##Im +=int(0.2 * np.random.random(Im.shape))
Im=cv2.GaussianBlur(Im,(3,3),0)


# ��ֵ������õ���ֵ��ͼ
##LimitIm=Im.convert('L') 


### �趨�Լ��ķֽ緧ֵɫ��
##threshold = 60
##table = []
##for i in range(256):
##    if i < threshold:
##        table.append(0)
##    else:
##        table.append(1)
##
###�任��ֵ��ɫ�淧ֵӦ�õ�ͼ��
##BrightIm=LimitIm.point(table,'1')

###CANNY��Ե��ȡ
##CannyFilterIm=LimitIm.filter(ImageFilter.FIND_EDGES)

#Compute the Canny filter for two values of sigma
##edges1 = feature.canny(Im)
##edges2 = feature.canny(Im, sigma=1)
##CannyFilterIm=feature.canny(Im,sigma=3)
edges = cv2.Canny(Im, 15, 200, apertureSize = 3)

#HOUGH�任�õ�ֱ��
minLineLength = 100
maxLineGap = 10
lines = cv2.HoughLines(edges,1,np.pi/180,118)
result = Im.copy()
lines = cv2.HoughLinesP(edges,1,np.pi/180,80,minLineLength,maxLineGap)
for x1,y1,x2,y2 in lines[0]:
	cv2.line(Im,(x1,y1),(x2,y2),(0,255,0),2)

#��ʾ���
#im.show()
##LimitIm.show()
#BrightIm.show()
#CannyFilterIm.show()

# display results
##fig, (ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=3, figsize=(8, 3), sharex=True, sharey=True)
##
##ax1.imshow(Im, cmap=plt.cm.jet)
##ax1.axis('off')
##ax1.set_title('noisy image', fontsize=20)
##
##ax2.imshow(edges2, cmap=plt.cm.gray)
##ax2.axis('off')
##ax2.set_title('Canny filter, $\sigma=1$', fontsize=20)
##
##ax3.imshow(CannyFilterIm, cmap=plt.cm.gray)
##ax3.axis('off')
##ax3.set_title('Canny filter, $\sigma=3$', fontsize=20)
##
##fig.subplots_adjust(wspace=0.02, hspace=0.02, top=0.9,
##                    bottom=0.02, left=0.02, right=0.98)
##plt.show()



#����任�����
##result = Im.copy()
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
cv2.imshow('Canny', edges )
cv2.imshow('Result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()


#������





