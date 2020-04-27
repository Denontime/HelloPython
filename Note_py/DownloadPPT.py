'''
@Descripttion: Null
@version: 1.0
@Author: Mar Ping
@Date: 2020-04-21 14:20:03
@LastEditors: Mar Ping
@LastEditTime: 2020-04-23 22:15:22
'''
import requests
import os
import PPT_OCR

def path_make(path):
    state = os.path.exists(path)

    if state != True:
        os.makedirs(path)

path_make(main_dir + r'\KTP_PPT\\' + str(file))

# 遍历每一个图片网址
for i in range(1,PPT_OCR.sum_pic):
    # 网址拼接, 构造完整的图片网址
    url = 'https://img.ketangpai.com/ketangpai.aliapp.com/1/webroot/Uploads/Download/2020-04-13/5e9469b805f12/'
    url_pic = url + str(i) + '.png'
    # 获取图片信息
    picture = requests.get(url_pic)

    with open(main_dir + r'\KTP_PPT\\' + str(file) + str(i) + '.jpg', 'wb') as f:
        f.write(picture.content)

    print('正在下载.........',end='\r')
print('........................程序执行完毕!........................')

