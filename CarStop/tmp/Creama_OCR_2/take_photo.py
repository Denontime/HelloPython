'''
@Descripttion: Null
@version: 1.0
@Author: Mar Ping
@Date: 2020-01-06 23:32:32
@LastEditors  : Mar Ping
@LastEditTime : 2020-01-17 14:27:23
'''

import cv2

def get_photo():
    #cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    cap = cv2.VideoCapture(1,cv2.CAP_DSHOW)        #启用摄像头  1内部/0外部

    while(1):

        ret, frame = cap.read()

        k = cv2.waitKey(1)                         #等待输入，参数为刷新率

        if k == ord('s'):

            cv2.imwrite('D:/Object/Python/CarStop/CarPhoto/Car.jpg', frame)     #保存图片
            cap.release()
            cv2.destroyAllWindows()     #释放窗口和摄像头
            break

        
        cv2.imshow("capture", frame)                #窗口显示图片

    cap.release()
    cv2.destroyAllWindows()  # 释放窗口和摄像头
    
    return ret 
