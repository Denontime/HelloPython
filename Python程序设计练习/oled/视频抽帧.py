'''
@Descripttion: Null
@version: 1.0
@Author: Mar Ping
@Date: 2019-12-04 00:01:57
@LastEditors: Mar Ping
@LastEditTime: 2020-05-11 14:38:10
'''
# File: pizza.py
# Program calculation the price(价格) per square inch(每平方英寸) of pizza
# by: Mar Ping

# -*- coding:utf8 -*-

import cv2
import os
import numpy
import shutil

#视频文件名字
filename = input("请输入视频文件名（带扩展名）：")


#保存图片的路径

savedpath = os.getcwd()

isExists = os.path.exists(savedpath)

if not isExists:

    os.makedirs(savedpath)

    print('path of %s is build'%(savedpath))

else:

    shutil.rmtree(savedpath)

    os.makedirs(savedpath)

    print('path of %s already exist and rebuild'%(savedpath))


#视频帧率
fps = input("请输入视频帧速率：")

#保存图片的帧率间隔
count = input("请输入抽帧间隔：")
count = float(count)
fps = float(fps)
cut = count / fps
print('每隔%f秒抽一帧图片'%(cut))



size_state = input("是否需要裁剪？[y/n]")
if(size_state == 'y'):
    cut_x1 =input("请输入左上角x坐标：")
    cut_y1 =input("请输入左上角y坐标：")
    cut_x2 =input("请输入右下角x坐标：")
    cut_y2 =input("请输入右下角y坐标：")


font_state = input("是否需要缩放？[y/n]")
if(font_state == 'y'):
    x = input("请输入原视频宽：")
    y = input("请输入原视频高：")
    tx = input("请输入导出图片宽：")
    ty = input("请输入导出图片高：")

    px = float(tx) / float(x)
    py = float(ty) / float(y)

colorstate = input("是否需要二值化？[y/n]")

if(colorstate == 'y'):
    brstate = input("手动[h] or 自动[a]?")
    
    if(brstate == 'h'):
        colormode = input("请输入二值化阈值：")

#开始读视频
videoCapture = cv2.VideoCapture(filename)

i = 0
j = 0


while True:

    success,resized = videoCapture.read()

    i +=1

    if(i % count ==0):

        j += 1
        
        #裁切图片
        if(size_state == 'y'):
            cropped = resized[cut_y1:cut_y2, cut_x1:cut_x2]
        #缩放图片
        if(font_state == 'y'):
            resized = cv2.resize(cropped, None, fx=px, fy=py, interpolation=cv2.INTER_AREA)
        #二值化图片
        if(colorstate == 'y'):

            if(brstate == 'h'):

                gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
                ret, resized = cv2.threshold(gray, colormode, 255, cv2.THRESH_TRUNC)

            elif(brstate == 'a'):

                gray = cv2.cvtColor(resized, cv2.COLOR_RGB2GRAY)  #把输入图像灰度化
                h, w =gray.shape[:2]
                m = numpy.reshape(gray, [1,w*h])
                mean = m.sum()/(w*h)
                print("mean:",mean)
                ret, resized =  cv2.threshold(gray, mean, 255, cv2.THRESH_BINARY)
        #命名
        savedname = str(j)+'.bmp'
        #保存图片
        cv2.imwrite(savedpath + savedname ,resized)

        print('image of %s is saved'%(savedname))
        print("保存路径：",savedpath)

    if not success:

        print('video is all read')

        break


