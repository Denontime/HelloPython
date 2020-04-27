'''
@Descripttion: Null
@version: 1.0
@Author: Mar Ping
@Date: 2020-04-25 20:35:31
@LastEditors: Mar Ping
@LastEditTime: 2020-04-26 00:25:32
'''
from PIL import Image

# 打开图片
im = Image.open('pic/[1].jpg')
# 得到图片大小
ims = im.size
print(ims[0],ims[1])
print(im.size)
# 图片格式
'''
print(im.format)
# 图片色彩模式
print(im.mode)
# 返回 ImagePalette 实例
print(im.palette)
# 实例信息（dict）
print(im.info)
#查看图片通道
print(im.getbands())
#改变尺寸
out = im.resize((2180, 1300))
# 打开，并查看图片
out.show()
im.show()
# 彩色变黑白
im = im.convert("L")
im.show()
'''