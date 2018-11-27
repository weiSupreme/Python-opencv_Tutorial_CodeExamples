import cv2 as cv
import numpy as np
#import matplotlib as plt

img = cv.imread('water_coins.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)
cv.imshow('thresh', thresh)
cv.waitKey(0)

kernel = np.ones((3, 3), dtype='uint8')
opening = cv.morphologyEx(thresh, cv.MORPH_OPEN, kernel, iterations=2)
cv.imshow('opening', opening)
cv.waitKey(0)

sure_bg = cv.dilate(opening, kernel, iterations=3)
cv.imshow('sure_bg', sure_bg)
cv.waitKey(0)

dist_transform = cv.distanceTransform(opening, cv.DIST_L2, 5)
ret, sure_fg = cv.threshold(dist_transform, 0.7 * dist_transform.max(), 255, 0)
cv.imshow('sure_fg', sure_fg)
cv.waitKey(0)

sure_fg = np.uint8(sure_fg)
unknown = cv.subtract(sure_bg, sure_fg)
cv.imshow('unknown', unknown)
cv.waitKey(0)

# Marker labelling
ret, markers = cv.connectedComponents(sure_fg)
# Add one to all labels so that sure background is not 0, but 1
markers = markers + 1
# Now, mark the region of unknown with zero
markers[unknown == 255] = 0
cv.imshow('markers', markers*255)
cv.waitKey(0)

markers = cv.watershed(img, markers)
img[markers == -1] = [255, 0, 0]
cv.imshow('img', img)
cv.waitKey(0)