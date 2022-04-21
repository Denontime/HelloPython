'''
Descripttion: Null
version: 1.0
Author: Mar Ping
Date: 2021-03-19 08:08:40
LastEditors: Mar Ping
LastEditTime: 2021-03-22 00:16:21
'''
import time

# with open("log_data_temp.txt", 'r', encoding="utf-8") as page: 
#     for line in page.readlines():
#         print(eval(line)['Values']['Voltage'])
#         # print(line)

# str2 = {'key': 19, 'time': 1616302454.4069605, 'ip': '127.0.0.1', 'port': 9011, 'data': 'aa5500200201010021780b0e1a013f106810681068050000100000102000000010301000ba12', 'Values': {'length': 32, 'function': 2, 'Type': 1, 'version': 1, 'Device_Id': 33, 'Voltage': 120, 'Up_Current': 11, 'Mid_Current': 14, 'Down_Current': 26, 'Internet_Status': 1, 'Motor_Status': 63, 'Up_Speed': 4200, 'Mid_Speed': 4200, 'Down_Speed': 4200, 'Pe_Status': 5, 'Fault': '00001000001020000000103010', 'Reserve': 0, 'Crc': 47634}}
# str3 = str2['Values']['Voltage']
# print(str2["Values"]["Voltage"])

# str1 = {"19":{"time":"1616298453.5058572","ip":"127.0.0.1","data":"aa5500200201010021780b0e1a013f106810681068050000100000102000000010301000ba12"}}
# data = str1["19"]["data"]
# Voltage = data[30:34]

# print(int(Voltage, 16))
'''
data = "aa5500200201010021780b0e1a013f106810681068050000100000102000000010301000ba12"
client = ("127.0.0.1", 9011)
Receive_count = 1
now = time.time()

length          = int(data[4:8], 16)
function        = int(data[8:10], 16)
Type            = int(data[10:12], 16)
version         = int(data[12:14], 16)
Device_Id       = int(data[14:18], 16)
Voltage         = int(data[18:20], 16)
Up_Current      = int(data[20:22], 16)
Mid_Current     = int(data[22:24], 16)
Down_Current    = int(data[24:26], 16)
Internet_Status = int(data[26:28], 16)
Motor_Status    = int(data[28:30], 16)
Up_Speed        = int(data[30:34], 16)
Mid_Speed       = int(data[34:38], 16)
Down_Speed      = int(data[38:42], 16)
Pe_Status       = int(data[42:44], 16)
Fault           = data[44:70]
Reserve         = int(data[70:72], 16)
Crc             = int(data[72:76], 16)


Dict = {
    "key": Receive_count,
    "time": now,
    "ip": client[0],
    "port": client[1],
    "data": data,
    "Values": {
        "length": length,
        "function": function,
        "Type": Type,
        "version": version,
        "Device_Id": Device_Id,
        "Voltage": Voltage,
        "Up_Current": Up_Current,
        "Mid_Current": Mid_Current,
        "Down_Current": Down_Current,
        "Internet_Status": Internet_Status,
        "Motor_Status": Motor_Status,
        "Up_Speed": Up_Speed,
        "Mid_Speed": Mid_Speed,
        "Down_Speed": Down_Speed,
        "Pe_Status": Pe_Status,
        "Fault": Fault,
        "Reserve": Reserve,
        "Crc": Crc
        }
}

print(str(Dict))
'''
def Format(line):
    str1 = []
    for i in range(0, len(line), 2):
        str1.append(line[i:i+2])
    return' '.join(str1)

fenge('00001000001020000000103010')
