import cv2
import numpy as np

def nothing(x):
    pass

cv2.namedWindow('img',cv2.WINDOW_AUTOSIZE)

cv2.createTrackbar('light','img',0,100,nothing)
cv2.setTrackbarPos('light','img',40)
cv2.createTrackbar('contrast','img',0,50,nothing)
cv2.setTrackbarPos('contrast','img',10)
cv2.createTrackbar('blur','img',0,130,nothing)
cv2.setTrackbarPos('blur','img',50)

img = cv2.imread('C:/Users/Dell/Desktop/C1(1)/C1/C1_0.bmp',1)
while(1):
    alpha=cv2.getTrackbarPos('light','img')
    beta=cv2.getTrackbarPos('contrast','img')
    s=int(cv2.getTrackbarPos('blur','img')/10)
    size=s if s%2==1 else s+1
    
    img1=img.astype('int16')
    img1=img1*(alpha/40)
    mean=cv2.blur(img1,(size,size))
    mean=mean.astype('int16')
    sub=img1-mean
    img1=sub*beta/10+img1
    img1[img1<0]=0
    img1[img1>255]=255
    img1=img1.astype('uint8')
    
    alphaLast=alpha
    betaLast=beta

    cv2.imshow('img',img1)
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()