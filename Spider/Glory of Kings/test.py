'''
@Descripttion: Null
@version: 1.0
@Author: Mar Ping
@Date: 2020-03-31 20:12:37
@LastEditors: Mar Ping
@LastEditTime: 2020-03-31 20:21:16
'''
import os

def path_make(path):
    state = os.path.exists(path)
    print(state)
    if state != True:
        os.makedirs(r'%s' % path)


path_make('D:\\Kings')
