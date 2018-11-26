import cv2
import numpy as np

img1 = cv2.imread('meci.jpg')
img2 = cv2.imread('opencvLogo.jpg')

rows, columns, c = img2.shape
roi = img1[0:rows, 0:columns]

img2Gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2Gray, 10, 255, cv2.THRESH_BINARY)
maskInv3 = np.zeros((rows, columns, c), dtype='uint8')
mask3 = np.zeros((rows, columns, c), dtype='uint8')
mask3[:, :, 0] = mask
mask3[:, :, 1] = mask
mask3[:, :, 2] = mask
maskInv3[:, :, 0] = cv2.bitwise_not(mask)
maskInv3[:, :, 1] = cv2.bitwise_not(mask)
maskInv3[:, :, 2] = cv2.bitwise_not(mask)
cv2.imshow('maskInv', maskInv3)
cv2.waitKey(0)

img2Fg = np.zeros((rows, columns, c), dtype='uint8')
img2Fg[:, :, 0] = cv2.bitwise_and(img2[:, :, 0], img2[:, :, 0], mask=mask3[:, :, 0])
img2Fg[:, :, 1] = cv2.bitwise_and(img2[:, :, 1], img2[:, :, 1], mask=mask3[:, :, 1])
img2Fg[:, :, 2] = cv2.bitwise_and(img2[:, :, 2], img2[:, :, 2], mask=mask3[:, :, 2])

img1Bg = np.zeros((rows, columns, c), dtype='uint8')
img1Bg[:, :, 0] = cv2.bitwise_and(roi[:, :, 0], roi[:, :, 0], mask=maskInv3[:, :, 0])
img1Bg[:, :, 1] = cv2.bitwise_and(roi[:, :, 1], roi[:, :, 1], mask=maskInv3[:, :, 1])
img1Bg[:, :, 2] = cv2.bitwise_and(roi[:, :, 2], roi[:, :, 2], mask=maskInv3[:, :, 2])

dst = cv2.add(img1Bg, img2Fg)
img1[0:rows, 0:columns] = dst

cv2.imshow('res', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
