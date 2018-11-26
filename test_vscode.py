import cv2

img = cv2.imread('C:/Users/Dell/Desktop/C1(1)/C1/C1_0.bmp',-1)
cv2.namedWindow('img',cv2.WINDOW_NORMAL)
cv2.circle(img,(327,244),20,(0,0,0),3)
cv2.rectangle(img,(0,0),(255,255),(127,234,86),5)
cv2.imshow('img',img)
cv2.waitKey(0)