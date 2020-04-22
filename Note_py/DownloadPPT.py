'''
@Descripttion: Null
@version: 1.0
@Author: Mar Ping
@Date: 2020-04-21 14:20:03
@LastEditors: Mar Ping
@LastEditTime: 2020-04-21 15:32:31
'''
import requests
import os


def path_make(path):
    state = os.path.exists(path)

    if state != True:
        os.makedirs(path)

path_make("D:\\Files\\Spider\\2.2.0\\")

# 遍历每一个图片网址
for i in range(1,18):
    # 网址拼接, 构造完整的图片网址
    url = 'https://img.ketangpai.com/ketangpai.aliapp.com/1/webroot/Uploads/Download/2020-04-13/5e9469b805f12/'
    url_pic = url + str(i) + '.png'
    # 获取图片信息
    picture = requests.get(url_pic)

    with open('D:/Files/Spider/2.2.0/' + str(i) + '.jpg', 'wb') as f:
        f.write(picture.content)

    print('正在下载.........',end='\r')
print('........................程序执行完毕!........................')

