import os
import time 
import datetime

#建议将log文件后缀改成txt进行处理，否则容易出现问题

filepath1 = 'Scanner log.txt'          #scanner文件路径
filepath2 = 'PLC下降沿时间.txt'          #PLC文件路径
savepath = 'newMore.txt'               #保存路径

with open(filepath1, 'r') as Scanner:
    with open(filepath2, 'r') as PLC:
        with open(savepath,'w+') as newPLC:
            while True:
                line = PLC.readline()[11:23]
                msg = Scanner.readline()[53:]
                if not line:      #等价于if line == "":
                    break
                if not msg:      #等价于if line == "":
                    break
                line = line.replace(r'.',':')
                ret = line.split(':')
                msg = msg.rstrip('\n')
                rot = msg.split(':')
                # print(ret)
                # print(rot)
                time1 = datetime.timedelta(hours=int(ret[0]),minutes=int(ret[1]),seconds=int(ret[2]),milliseconds=int(ret[3]))
                time2 = datetime.timedelta(hours=int(rot[0]),minutes=int(rot[1]),seconds=int(rot[2]),milliseconds=int(rot[3]))
                # print(time2-time1)
                # newPLC.write(line + ' --- ' + msg + ' --- ' + str(time2-time1) + '\n')
                # newPLC.write(line + ' --- ' + msg + ' --- ' + str((time2-time1).microseconds) + '\n') #输出原数据与时间差
                newPLC.write(str((time2-time1).microseconds) + '\n')    #只输出时间差


