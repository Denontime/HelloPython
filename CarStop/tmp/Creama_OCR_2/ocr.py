'''
@Descripttion: Null
@version: 1.0
@Author: Mar Ping
@Date: 2020-01-02 22:13:41
@LastEditors  : Mar Ping
@LastEditTime : 2020-01-17 14:44:01
'''
""" 包 """
from aip import AipOcr
import time
import cv2
#import os

"""文件"""
#import take_photo
import key

#Photo_Path = 'D:/Object/Python/CarStop/CarPhoto/Car.jpg'

""" 读取图片 ""
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

"""""""""""""""""""""""""""""""""""""""
while (1):
    
    #take_photo.get_photo()                   #拍摄图片

    #image = get_file_content(Photo_Path)      #读取图片
    cam = cv2.VideoCapture(1,cv2.CAP_DSHOW)
    
    ret, image = cam.read()
    #os.remove(Photo_Path)                     #删除图片

    if ret == True:
        """ 调用车牌识别 """
        result = key.client.licensePlate(image)
        
        """获取车牌数据"""
        #if result.get('words_result',default=False):
        if 'words_result' in result:
            carl_color = result['words_result']['color']
            carl_number = result['words_result']['number']
            break
        else:
            continue
        
        print('车牌颜色 ：'+carl_color)
        print('车牌号码 ：'+carl_number,end='\n')
    
    else:
        continue

