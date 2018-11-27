import cv2 as cv
import numpy as np
import matplotlib as plt

img = cv.imread('hist.jpg', 0)
mask = np.zeros(img.shape[:2], dtype='uint8')
mask[50:150, 100:200] = 255
maskImg = cv.bitwise_and(img, img, mask=mask)

histFull = cv.calcHist([img], [0], None, [256], [0, 256])
histMask = cv.calcHist([img], [0], mask, [256], [0, 256])

cv.imshow('img', img)
cv.imshow('maskimg', maskImg)
cv.imshow('histfull', histFull)
cv.imshow('histmask', histMask)

plt.subplot(221), plt.imshow(img, 'gray')
plt.subplot(222), plt.imshow(mask, 'gray')
plt.subplot(223), plt.imshow(maskImg, 'gray')
plt.subplot(224), plt.plot(histFull), plt.plot(histMask)
plt.xlim([0, 256])
plt.show()