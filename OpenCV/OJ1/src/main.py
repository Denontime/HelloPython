import cv2

img1 = cv2.imread('image/wood.jpg',cv2.IMREAD_UNCHANGED)
img2 = cv2.cvtColor(img1,cv2.COLOR_RGB2GRAY)

cv2.imshow('Image1',img1)
cv2.imshow('Image2',img2)

cv2.waitKey(0)

cv2.destroyAllWindow()     #销毁所有窗口
