'''
@Descripttion: Null
@version: 1.0
@Author: Mar Ping
@Date: 2020-04-21 16:18:04
@LastEditors: Mar Ping
@LastEditTime: 2020-04-23 23:16:20
'''
from aip import AipOcr
import os

#"""""""""""""""""""""“"""权限证书"""""""""""""""""""""""""""""
APP_ID = '19534018'
API_KEY = 'dgHolPV3cciGmfZusoys5kyg'
SECRET_KEY = '74HQMDvmoAf6C0kjtU3oYm4TRcbNAjqL'
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

#"""""""""""""""""""""“"""获取图片"""""""""""""""""""""""""""""
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

def ocr():
#"""""""""""""""""""""“”"""识别"""""""""""""""""""""""""""""""
    result = ''
    sum_pic = 0
    try:
        for i in range(1,100):
            image = get_file_content('pic/' + '(' + str(i) + ')' + '.bmp')
            basic_mode = client.basicAccurate(image)
            sum_words = basic_mode['words_result_num']
            for i in range(0, sum_words):
                if i == 0:
                    result = result + '    ' + \
                        str(basic_mode['words_result'][i]['words'])
                else:
                    result = result + str(basic_mode['words_result'][i]['words'])
            result = result + '\n\n'
            sum_pic = sum_pic + 1
    except IOError:
        return result,sum_pic

