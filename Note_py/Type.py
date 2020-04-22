'''
@Descripttion: Null
@version: 1.0
@Author: Mar Ping
@Date: 2020-04-21 17:20:38
@LastEditors: Mar Ping
@LastEditTime: 2020-04-21 17:45:26
'''
import json

word = {'log_id': 7704648003679712757, 'words_result_num': 4, 'words_result': [
    {'words': '计算机网络概述'}, {'words': '银川能源学院'}, {'words': '信息传媒学院'}, {'words': '丁永贤'}]}
word_A = word['words_result']
word_B = word_A[1]
print(word_B['words'])
for i in range(0,4):
    print(word['words_result'][i]['words'])
#print (json.dumps(word, sort_keys=True, indent=4, separators=(',', ': ')))
