import cv2 as cv
import numpy as np

img = cv.imread('perspectiveTrans.bmp')
pts1 = np.float32([[133, 235], [497, 225], [489, 278], [128, 273]])
pts2 = np.float32([[20, 235], [610, 225], [610, 278], [20, 273]])

M = cv.getPerspectiveTransform(pts1, pts2)
dst = cv.warpPerspective(img, M, (656, 490))

img1 = cv.imread('perspectiveTrans1.bmp')
pts3 = np.float32([[2, 144], [207, 110], [236, 445], [39, 448]])
pts4 = np.float32([[0, 0], [327, 0], [327, 489], [0, 489]])
#pts3 = np.float32([[2, 144], [410, 126], [419, 416], [39, 448]])
#pts4 = np.float32([[0, 0], [655, 0], [655, 489], [0, 489]])
M1 = cv.getPerspectiveTransform(pts3, pts4)
dst1 = cv.warpPerspective(img1, M1, (656, 490))

cv.imshow('result', dst1)
cv.waitKey(0)