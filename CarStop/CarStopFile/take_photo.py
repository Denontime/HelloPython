'''
@Descripttion: Null
@version: 1.0
@Author: Mar Ping
@Date: 2020-01-06 23:32:32
@LastEditors  : Mar Ping
@LastEditTime : 2020-01-06 23:37:55
'''


import cv2


cap = cv2.VideoCapture(0)

i = 0

while(1):

    ret, frame = cap.read()

    k = cv2.waitKey(1)

    if k == 27:

        break

    elif k == ord('s'):

        cv2.imwrite('D:\\Files\\'+str(i)+'.jpg', frame)

        i += 1

    cv2.imshow("capture", frame)

cap.release()

cv2.destroyAllWindows()
