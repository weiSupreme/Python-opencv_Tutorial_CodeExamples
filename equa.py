import cv2 as cv

img = cv.imread('equahist.bmp', 0)
res = cv.equalizeHist(img)
cv.imshow('res', res)
cv.waitKey(0)