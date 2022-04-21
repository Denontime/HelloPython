'''
@Descripttion: Null
@version: 1.0
@Author: Mar Ping
@Date: 2020-01-02 22:13:41
@LastEditors  : Mar Ping
@LastEditTime : 2020-01-09 00:12:54
'''
""" 包 """
from aip import AipOcr
import time
import cv2
import os

"""文件"""
import take_photo
import key

Photo_Path = 'D:/Object/Python/CarStop/CarPhoto/Car.jpg'

""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

""""""""""""""""""""""""""""""""""""""""""""""""""""""
while (1):
    
    take_photo.get_photo()                   #拍摄图片

    image = get_file_content(Photo_Path)      #读取图片

    os.remove(Photo_Path)                     #删除图片

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
print('车牌号码 ：'+carl_number)
print()

