'''
@Descripttion: Null
@version: 1.0
@Author: Mar Ping
@Date: 2020-04-21 18:01:30
@LastEditors: Mar Ping
@LastEditTime: 2020-04-23 22:14:01
'''
from aip import AipOcr
import os
import DownloadPPT
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
APP_ID = '19534018'
API_KEY = 'dgHolPV3cciGmfZusoys5kyg'
SECRET_KEY = '74HQMDvmoAf6C0kjtU3oYm4TRcbNAjqL'
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
file = "2.3"
sum_pic = 38
path = "D:/Files/Spider/"

for i in range(1,sum_pic+1):
    image = get_file_content(path + file + '/' + str(i) +'.jpg')
    basic_mode = client.basicAccurate(image)
    sum_words = basic_mode['words_result_num']
    result = ''
    for i in range(0, sum_words):
        result = result + str(basic_mode['words_result'][i]['words']) + '\n'
    with open(path + file + '.txt', 'a') as f:
        f.write(result)
print(".................................执行成功！....................................")