import cv2
import numpy as np
ix=0
iy=0
drawing=False
img=[]
img1=[]
img2=[]
def MouseDraw(events,x,y,flags,param):
    global ix,iy,drawing,img,img1,img2
    if events==cv2.EVENT_LBUTTONDOWN:
        drawing=True
        ix=x
        iy=y
    if events==cv2.EVENT_MOUSEMOVE:
        if drawing:
            img2=img1.copy()
            radius=int(np.sqrt((x-ix)*(x-ix)+(y-iy)*(y-iy)))
            cv2.circle(img2,(ix,iy),radius,(127,234,86),1)
            img=img2.copy()
    if events==cv2.EVENT_LBUTTONUP:
        drawing=False
        img1=img.copy()

img = cv2.imread('C:/Users/Dell/Desktop/C1(1)/C1/C1_0.bmp',1)
img1=img.copy()
cv2.namedWindow('img',cv2.WINDOW_NORMAL)
cv2.setMouseCallback('img',MouseDraw)
while(1):
    cv2.imshow('img',img)
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()