import cv2 as cv
import numpy as np

img = cv.imread('j.png')
kernel = np.ones((3, 3), dtype='uint8')

erosion = cv.erode(img, kernel, iterations=1)
cv.imshow('erosion', erosion)
cv.waitKey(0)

dilation = cv.dilate(img, kernel, iterations=1)
cv.imshow('dilation', dilation)
cv.waitKey(0)
