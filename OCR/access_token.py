'''
@Descripttion: Null
@version: 1.0
@Author: Mar Ping
@Date: 2019-12-03 19:41:22
@LastEditors: Mar Ping
@LastEditTime: 2019-12-03 19:46:55
'''
# -*- coding: utf-8 -*- 
#!/usr/bin/env python 
import urllib 
import urllib.parse 
import urllib.request 
import base64 
import json 
#client_id 为官网获取的AK， client_secret 为官网获取的SK 
client_id = 'rDNOOCWWK9yp3cbms5lzA7RP'
client_secret = '0YWaq0pFFcsap09gDA4PUcl9nixOQjcS'
#获取token 
def get_token(): 
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=' + \
    client_id + '&client_secret=' + client_secret
    request = urllib.request.Request(host) 
    request.add_header('Content-Type', 'application/json; charset=UTF-8') 
    response = urllib.request.urlopen(request) 
    token_content = response.read() 
    if token_content: 
        token_info = json.loads(token_content.decode("utf-8")) 
        token_key = token_info['access_token'] 
    return token_key 


get_token()
