'''
@Descripttion: Null
@version: 1.0
@Author: Mar Ping
@Date: 2020-05-13 17:39:57
@LastEditors: Mar Ping
@LastEditTime: 2020-05-13 21:11:43
'''
lines = 0
array = 0
pic_array = 0
with open("Uint8Picture.txt",'r',encoding = "utf-8") as pic:
    for line in pic.readlines():
        lines += 1
        with open('Uint8Picture-ino.txt', 'a') as ino:
            line = line[:80]
            ino.write(line)
        if(lines % 64 == 0):
            array += 1
            if(array % 24 == 0):
                pic_array += 1
                with open('Uint8Picture-ino.txt', 'a') as ino:
                    ino.write('\n')
                    ino.write("}")
                    ino.write("//第%d副图片数组"%(array))
                    ino.write('\n')
                    ino.write("};")
                    ino.write("//第%d组图片"%(pic_array))
                    ino.write('\n')
                    ino.write('\n')
                    ino.write('\n')
                    ino.write("const unsigned char pic%d[][1024] U8X8_PROGMEM= {"%(pic_array))
                    ino.write('\n')
                    ino.write('{')
                    ino.write('\n')
            else:
                with open('Uint8Picture-ino.txt', 'a') as ino:
                    ino.write('\n')
                    ino.write("},")
                    ino.write("//第%d副图片数组"%(array))
                    ino.write('\n')
                    ino.write('\n')
                    ino.write('{')
                    ino.write('\n')


