# 导入OpenCV库
import cv2

# 读取图片
img = cv2.imread('images/st_2.jpeg')
# 转换为灰阶图片
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 人脸检测器
face_cascade = cv2.CascadeClassifier('lib/haarcascades/haarcascade_frontalface_default.xml')
faces = face_cascade.detectMultiScale(gray, 1.3, 5)

# 绘制人脸区域
for (x,y,w,h) in faces:
    print(x,y,w,h)
    '''****************BEGIN****************'''
    # 在人脸区域添加矩形框

    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
    face_areas = img[y:y+h, x:x+w]
    face_grays = gray[y:y+h, x:x+w]
    
    '''**************** END ****************'''

    #绘制眼睛区域
    path_of_haarcascade_eye = "lib/haarcascades/haarcascade_eye.xml"
    eye_cascade = cv2.CascadeClassifier(path_of_haarcascade_eye)
    eyes = eye_cascade.detectMultiScale(face_grays)
    '''****************BEGIN****************'''
    for (ex,ey,ew,eh) in eyes:
        print(ex,ey,ew,eh)
        # 在眼睛区域添加矩形框

        cv2.rectangle(face_areas,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

    '''**************** END ****************'''

# 保存图片
save_image_path = "out/st_2_drawing.jpg"
cv2.imwrite(save_image_path,img)
