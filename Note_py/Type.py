'''
@Descripttion: Null
@version: 1.0
@Author: Mar Ping
@Date: 2020-04-21 17:20:38
@LastEditors: Mar Ping
@LastEditTime: 2020-04-23 21:56:06
'''
import requests
import json


'''
word = {'log_id': 7704648003679712757, 'words_result_num': 4, 'words_result': [
    {'words': '计算机网络概述'}, {'words': '银川能源学院'}, {'words': '信息传媒学院'}, {'words': '丁永贤'}]}
word_A = word['words_result']
word_B = word_A[1]
print(word_B['words'])
for i in range(0,4):
    print(word['words_result'][i]['words'])
#print (json.dumps(word, sort_keys=True, indent=4, separators=(',', ': ')))
'''
url = 'https://www.ketangpai.com/PrestudyTask/study.html?interactid=MDAwMDAwMDAwMLOGpdyH39GxhbVyoQ&pageIndex=11.html'
result = requests.get(url)
result.encoding = 'utf-8'
print(result.text)


#https: // www.ketangpai.com/PrestudyTask/study.html?interactid = MDAwMDAwMDAwMLOGpdyH39GxhbVyoQ & pageIndex = 11
#https: // img.ketangpai.com/ketangpai.aliapp.com/1/webroot/Uploads/Download/2020-04-13/5e9469b805f12/11.png?OSSAccessKeyId = LTAItfPkNIKJFibY & Expires = 1596289210 & Signature = owEmOkvMaSVwr0bidiVHBXXuWs4 % 3D

