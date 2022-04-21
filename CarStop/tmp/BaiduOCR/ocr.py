'''
@Descripttion: Null
@version: 1.0
@Author: Mar Ping
@Date: 2020-01-02 22:13:41
@LastEditors  : Mar Ping
@LastEditTime : 2020-01-08 23:14:02
'''

from aip import AipOcr
import key

""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


image = get_file_content(
    'D:\\Object\\Python\\CarStop\\CarPhoto\\色图.jpg')

""" 调用车牌识别 """
result = key.client.licensePlate(image)

"""获取车牌数据"""
carl_color = result['words_result']['color']
carl_number = result['words_result']['number']

print(result)
print('车牌颜色 ：'+carl_color)
print('车牌号码 ：'+carl_number)

""" 如果有可选参数
options = {}
options["multi_detect"] = "true"
"""
""" 带参数调用车牌识别 
#client.licensePlate(image, options)
"""


