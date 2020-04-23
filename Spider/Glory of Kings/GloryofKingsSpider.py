'''
@Descripttion: Null
@version: 1.0
@Author: Mar Ping
@Date: 2019-12-18 18:09:10
@LastEditors: Mar Ping
@LastEditTime: 2020-04-23 20:55:52
'''
# 1.导入所需模块
import requests
import os

print('\n--------------------------------王者荣耀皮肤壁纸下载--------------------------------')
print('\n     本程序会下载当前版本王者荣耀官方公布的所有英雄的皮肤图片（包括英雄伴生皮肤），本程序仅供个')
print('\n人学习娱乐，所有文件版权为腾讯公司所有，不可用于商业用途，任何非正常使用造成的后果自负，与程序制')
print('\n作者无关！')
print('\n版本：v1.2')
print('\n更新说明：')
print('\n        现在会直接在程序所处的文件夹创建并开始下载，免去找文件夹的麻烦。')
print('                                                                               MPS')

input("按回车继续................")

def path_make(path):
    state = os.path.exists(path)
    if state != True :
        os.makedirs(path)

main_dir = os.getcwd()

path_make(main_dir)
print('\n图片保存路径 --> ', main_dir , end='\n')

# 2.读取json文件
url = 'http://pvp.qq.com/web201605/js/herolist.json'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'}  # 添加用户代理
response = requests.get(url, headers=headers)
json_list = response.json()

sum_hero = len(json_list)
print("\n当前版本英雄总数 ：",sum_hero,end='\n') # 英雄总数量：98个英雄
# print(json_list) # 打印结果,了解json_list的构造

try:
    # 3.提取json文件,下载图片
    for m in range(len(json_list)):
        # 英雄编号
        hero_num = json_list[m]['ename']
        # 英雄名称
        hero_name = json_list[m]['cname']
        # 获取皮肤列表
        skin_name = json_list[m]['skin_name'].split('|')
        # 统计皮肤数量
        skin_count = len(skin_name)
        print('英雄名称：', '%10s' % hero_name, '%15s' %' 皮肤数量：', skin_count, end='\n')  # 打印英雄的皮肤数量
        path_make(main_dir +r'\Glory of Kings' + '\\%s' % hero_name)

        # 遍历每一个图片网址
        for i in range(1, skin_count + 1):
            # 网址拼接, 构造完整的图片网址
            url = 'http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/'  # 图片网址固定前缀
            url_pic = url + str(hero_num) + '/' + str(hero_num) + '-bigskin-' + str(i) + '.jpg'
            # 获取图片信息
            picture = requests.get(url_pic).content
            # print(picture) # 打印图片网址
            # 下载图片 文件路径为: pic/英雄名-皮肤名.jpg (需要新建pic文件夹)
            
            with open(main_dir + r'\Glory of Kings' + '\\' + '%s' % hero_name + '\\' + skin_name[i - 1] + '.jpg', 'wb') as f:
                f.write(picture)
            percent = 1.0 * m / sum_hero * 100
            print('正在下载.........', '%.1f' % percent, '%',end='\r')

except KeyError as e:
    # 捕获异常：解决皮肤名称全部打印完成后会报错的问题
    print('........................程序执行完毕!........................')
    print('\n图片保存路径 --> ', main_dir, end='\n')

input("按回车结束运行................")
