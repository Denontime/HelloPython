'''
Descripttion: Null
version: 1.0
Author: Mar Ping
Date: 2021-03-20 19:50:09
LastEditors: Mar Ping
LastEditTime: 2021-03-21 15:24:38
'''
# -*- coding: utf-8 -*-

import binascii
import socket  # 导入socket模块
import time  # 导入time模块

      #server 接收端
      # 设置服务器默认端口号
PORT = 9022
      # 创建一个套接字socket对象，用于进行通讯
      # socket.AF_INET 指明使用INET地址集，进行网间通讯
      # socket.SOCK_DGRAM 指明使用数据协议，即使用传输层的udp协议
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
address = ("127.0.0.1", PORT)  
server_socket.bind(address)  # 为服务器绑定一个固定的地址，ip和端口
# server_socket.settimeout(5)  #设置一个时间提示，如果10秒钟没接到数据进行提示
Receive_count = 0
while True:
	#正常情况下接收数据并且显示，如果10秒钟没有接收数据进行提示（打印 "time out"）
	#当然可以不要这个提示，那样的话把"try:" 以及 "except"后的语句删掉就可以了
    # try:  
        now = time.time()  #获取当前时间

                        # 接收客户端传来的数据 recvfrom接收客户端的数据，默认是阻塞的，直到有客户端传来数据
                        # recvfrom 参数的意义，表示最大能接收多少数据，单位是字节
                        # recvfrom返回值说明
                        # receive_data表示接受到的传来的数据,是bytes类型
                        # client  表示传来数据的客户端的身份信息，客户端的ip和端口，元组
        receive_data, client = server_socket.recvfrom(1024)
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(now)))  #以指定格式显示时间
        data = binascii.b2a_hex(receive_data).decode('utf-8')
        
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
        with open("log_data_temp.txt", 'a', encoding="utf-8") as log:
            Receive_count = Receive_count + 1
            log.writelines(str(Dict)+'\n')

    # except socket.timeout:  #如果10秒钟没有接收数据进行提示（打印 "time out"）
    #     print("tme out")
