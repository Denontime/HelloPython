'''
@Descripttion: Null
@version: 1.0
@Author: Mar Ping
@Date: 2020-04-21 16:18:04
@LastEditors: Mar Ping
@LastEditTime: 2020-04-21 18:00:55
'''
from aip import AipOcr
import os

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
image = get_file_content('3.jpg')

basic_mode = client.basicAccurate(image)

sum_words = basic_mode['words_result_num']
result = ''

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
for i in range(0, sum_words):
    result = result + str(basic_mode['words_result'][i]['words']) + '\n'
print(result)

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
with open('basic_mode.txt', 'w') as f:
        f.write(result)

#print(high_mode)
#print(basic_mode)
