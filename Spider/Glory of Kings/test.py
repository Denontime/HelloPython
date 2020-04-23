'''
@Descripttion: Null
@version: 1.0
@Author: Mar Ping
@Date: 2020-03-31 20:12:37
@LastEditors: Mar Ping
@LastEditTime: 2020-04-23 17:55:24
'''
import os

def path_make(path):
    state = os.path.exists(path)
    print(state)
    if state != True:
        os.makedirs(r'%s' % path)



def convert_path(path: str) -> str:
    return path.replace(r'\/'.replace(os.sep, ''), os.sep)


print(convert_path(r'C: \Users\27132\Desktop\新建文件夹'))
