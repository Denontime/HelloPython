'''
@Descripttion: Null
@version: 1.0
@Author: Mar Ping
@Date: 2020-01-06 23:32:32
@LastEditors  : Mar Ping
@LastEditTime : 2020-01-08 21:57:17
'''

import cv2

def get_photo():
    #cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    cap = cv2.VideoCapture(1,cv2.CAP_DSHOW)

    while(1):

        ret, frame = cap.read()

        k = cv2.waitKey(1)

        if k == ord('s'):

            cv2.imwrite('D:/Object/Python/CarStop/CarPhoto/Car.jpg', frame)
            cap.release()
            cv2.destroyAllWindows()
            break

        
        cv2.imshow("capture", frame)

    cap.release()
    cv2.destroyAllWindows()
    
    return ret 
