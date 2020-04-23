'''
@Descripttion: Null
@version: 1.0
@Author: Mar Ping
@Date: 2020-04-23 16:03:34
@LastEditors: Mar Ping
@LastEditTime: 2020-04-23 23:17:24
'''
#百度通用翻译API,不包含词典、tts语音合成等资源，如有相关需求请联系translate_api@baidu.com
# coding=utf-8

import http.client
import hashlib
import urllib
import random
import json
import OCR_PPT

'''
APP ID：20200423000427835
密钥：FOLMEw55s5AxeAIY2fyO
'''
appid = '20200423000427835'  
secretKey = 'FOLMEw55s5AxeAIY2fyO'  

httpClient = None
myurl = '/api/trans/vip/translate'

fromLang = 'auto'   #原文语种
toLang = 'zh'   #译文语种
salt = random.randint(32768, 65536)
ocr = OCR_PPT.ocr()
q = ocr[0]

sign = appid + q + str(salt) + secretKey
sign = hashlib.md5(sign.encode()).hexdigest()
myurl = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(
salt) + '&sign=' + sign

trs_result = ''
try:
    httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
    httpClient.request('GET', myurl)

    # response是HTTPResponse对象
    response = httpClient.getresponse()
    result_all = response.read().decode("utf-8")
    result = json.loads(result_all)

    for i in range(0,ocr[1]):
        trs_result = trs_result + '    ' + str(result['trans_result'][i]['dst'])
        trs_result = trs_result + '\n\n'
    print ("原文：", '\n', q, end='\n')
    print ("译文：", '\n', trs_result, end='\n')

except Exception as e:
    print (e)
finally:
    if httpClient:
        httpClient.close()
