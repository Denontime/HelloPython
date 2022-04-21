import cv2
#定义摄像头
cap = cv2.VideoCapture(0)


for i in range (10000):

    ret,frame = cap.read()#读取每一帧

    cv2.imshow('摄像头',frame)#显示每一帧

    if cv2.waitKey(1) & 0xFF == ord():

        break

cap.release()

cv2.destroyAllWindows()   
