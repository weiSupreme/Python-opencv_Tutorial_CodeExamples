import cv2
import numpy as np

img = np.ones((500, 500, 3), dtype='uint8')
img[:, :, 1] = img[:, :, 1] * 255
cv2.imshow('img', img)
hsvImg = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow('hsv', hsvImg)
print(hsvImg[0, 0, :])
cv2.waitKey(0)