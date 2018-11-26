import cv2

def MouseDraw(events,x,y,flags,param):
    if events==cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),20,(127,234,86),3)

img = cv2.imread('C:/Users/Dell/Desktop/C1(1)/C1/C1_0.bmp',1)
cv2.namedWindow('img',cv2.WINDOW_NORMAL)
cv2.setMouseCallback('img',MouseDraw)
while(1):
    cv2.imshow('img',img)
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()