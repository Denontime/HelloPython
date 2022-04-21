'''
Descripttion: Null
version: 1.0
Author: Mar Ping
Date: 2021-03-21 15:11:54
LastEditors: Mar Ping
LastEditTime: 2021-03-23 18:28:12
'''
import PySimpleGUI as sg
import threading
import binascii
import socket  # 导入socket模块
import time  # 导入time模块
import os

Filelock = threading.RLock()

PORT = 9022
OK = True
Dict = ''
Data_List = []
Data_List_Index = -1
Receive_count = 0
Receive_flag = False
Ip_address = []
Ip_State = ['']

def Get_Ip_List():
    if os.path.exists('Ip_List.txt'):
        with open('Ip_List.txt', 'r', encoding="utf-8") as file:
            Ip_List = file.read()
        return Ip_List
    else:
        with open('Ip_List.txt', 'w', encoding="utf-8") as file:
            pass
        return '[]'

def Save_Ip_List(Ip_List):
    with open('Ip_List.txt', 'w+', encoding="utf-8") as file:
        file.seek(0)
        file.truncate()
        file.write(Ip_List)
    return OK

def Format(line):
    str1 = []
    for i in range(0, len(line), 2):
        str1.append(line[i:i+2])
    return' '.join(str1)

def Socket():
    global Dict
    global Receive_count
    global Receive_flag
    global Ip_address
    global Data_List
    global Data_List_Index
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    address = ("127.0.0.1", PORT)  
    server_socket.bind(address)  # 为服务器绑定一个固定的地址，ip和端口
    # server_socket.settimeout(5)  #设置一个时间提示，如果10秒钟没接到数据进行提示
    while True:
        now = time.time()  #获取当前时间
        receive_data, client = server_socket.recvfrom(1024)
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(now)))  #以指定格式显示时间
        data = binascii.b2a_hex(receive_data).decode('utf-8')
        
        length          = int(data[4:8], 16)
        function        = int(data[8:10], 16)
        Device_Type     = int(data[10:14], 16)
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
        
        Filelock.acquire()
        Receive_flag = True
        Dict = {
            "key": Receive_count,
            "time": now,
            "ip": client[0],
            "port": client[1],
            "data": data,
            "Values": {
                "length": length,
                "function": function,
                "Device_Type": Device_Type,
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
                "Fault": Format(Fault),
                "Reserve": Reserve,
                "Crc": Crc
                }
        }
        
        if client[0] not in Ip_address:
            Ip_address.append(client[0])
        
        Data_List.append(Dict)
        Data_List_Index += 1
        
        Filelock.release()
        with open(client[0] + '_' + str(client[1]) + '.txt', 'a', encoding="utf-8") as log:
            Receive_count = Receive_count + 1
            log.writelines(str(Dict)+'\n')

def Ui():
    sg.theme('BrownBlue')
    Frame_Left_Layout = sg.Frame("Left",
                                        [[sg.Column([
                                                        [sg.Text('IP:'), sg.Input('', key='-Ip_Out-', readonly=True)],
                                                        [sg.Text('IP List:')],
                                                        [sg.Listbox(Ip_address, key='-IP-LIST-', size=(16, 15))],
                                                        [sg.Text("Port:"), sg.Input('9011', readonly=True)],
                                                        [sg.Exit()],
                                                    ],
                                                    size=(200, 700)
                                                    )
                                        ]]
                                )
    
    Frame_Right_Layout = sg.Frame("Right",
                                        [[sg.Column([
                                                        [sg.Text("Device_Id       "),sg.Input('', key='-Device_Id-', readonly=True)],
                                                        [sg.Text("Voltage         "),sg.Input('', key='-Voltage-', readonly=True)],
                                                        [sg.Text("Up_Current      "),sg.Input('', key='-Up_Current-', readonly=True)],
                                                        [sg.Text("Mid_Current     "),sg.Input('', key='-Mid_Current-', readonly=True)],
                                                        [sg.Text("Down_Current    "),sg.Input('', key='-Down_Current-', readonly=True)],
                                                        [sg.Text("Motor_Status    "),sg.Input('', key='-Motor_Status-', readonly=True)],
                                                        [sg.Text("Up_Speed        "),sg.Input('', key='-Up_Speed-', readonly=True)],
                                                        [sg.Text("Mid_Speed       "),sg.Input('', key='-Mid_Speed-', readonly=True)],
                                                        [sg.Text("Down_Speed      "),sg.Input('', key='-Down_Speed-', readonly=True)],
                                                        [sg.Text("Pe_Status       "),sg.Input('', key='-Pe_Status-', readonly=True)],
                                                        [sg.Text("Fault           "),sg.Multiline('', key='-Fault-', size=(38, 1))],
                                                        [sg.Button('<', key='-Prior-', image_size=(50,50)),
                                                        sg.Button('>', key='-Next-', image_size=(50,50))],
                                                    ],
                                                    size=(635, 700), element_justification='left'
                                                    )
                                        ]]
                                )

    layout = [[Frame_Left_Layout,Frame_Right_Layout]]
    window = sg.Window("IOT", layout, finalize=True, font='Consolas')

    return window

if __name__ == '__main__':
    Ip_Dic = eval(Get_Ip_List())
    print(Ip_Dic)
    my_thread = threading.Thread(target=Socket)
    Window = Ui()
    my_thread.setDaemon(True)
    my_thread.start()
    Ip_List = Window['-IP-LIST-']

    Ip_List.update(Ip_Dic)
    while True:
        event, values = Window.read(timeout=0)
        
        Ip_Out          = Window['-Ip_Out-']
        Ip_List         = Window['-IP-LIST-']
        Device_Id       = Window['-Device_Id-']
        Voltage         = Window['-Voltage-']
        Up_Current      = Window['-Up_Current-']
        Mid_Current     = Window['-Mid_Current-']
        Down_Current    = Window['-Down_Current-']
        Motor_Status    = Window['-Motor_Status-']
        Up_Speed        = Window['-Up_Speed-']
        Mid_Speed       = Window['-Mid_Speed-']
        Down_Speed      = Window['-Down_Speed-']
        Pe_Status       = Window['-Pe_Status-']
        Fault           = Window['-Fault-']
        
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        
        if event == '-Prior-':
            if Data_List_Index:
                Data_List_Index -= 1
            print(Data_List_Index)
            Device_Id.update(Data_List[Data_List_Index]['Values']['Device_Id'])
            Voltage.update(Data_List[Data_List_Index]['Values']['Voltage'])
            Up_Current.update(Data_List[Data_List_Index]['Values']['Up_Current'])
            Mid_Current.update(Data_List[Data_List_Index]['Values']['Mid_Current'])
            Down_Current.update(Data_List[Data_List_Index]['Values']['Down_Current'])
            Motor_Status.update(Data_List[Data_List_Index]['Values']['Motor_Status'])
            Up_Speed.update(Data_List[Data_List_Index]['Values']['Up_Speed'])
            Mid_Speed.update(Data_List[Data_List_Index]['Values']['Mid_Speed'])
            Down_Speed.update(Data_List[Data_List_Index]['Values']['Down_Speed'])
            Pe_Status.update(Data_List[Data_List_Index]['Values']['Pe_Status'])
            Fault.update(Data_List[Data_List_Index]['Values']['Fault'])

        if event == '-Next-':
            if Data_List_Index < len(Data_List)-1:
                Data_List_Index += 1
            print(Data_List_Index)
            Device_Id.update(Data_List[Data_List_Index]['Values']['Device_Id'])
            Voltage.update(Data_List[Data_List_Index]['Values']['Voltage'])
            Up_Current.update(Data_List[Data_List_Index]['Values']['Up_Current'])
            Mid_Current.update(Data_List[Data_List_Index]['Values']['Mid_Current'])
            Down_Current.update(Data_List[Data_List_Index]['Values']['Down_Current'])
            Motor_Status.update(Data_List[Data_List_Index]['Values']['Motor_Status'])
            Up_Speed.update(Data_List[Data_List_Index]['Values']['Up_Speed'])
            Mid_Speed.update(Data_List[Data_List_Index]['Values']['Mid_Speed'])
            Down_Speed.update(Data_List[Data_List_Index]['Values']['Down_Speed'])
            Pe_Status.update(Data_List[Data_List_Index]['Values']['Pe_Status'])
            Fault.update(Data_List[Data_List_Index]['Values']['Fault'])
        
        if values['-IP-LIST-']:
            Ip_State = values['-IP-LIST-']
        
        Ip_Out.update(Ip_State[0])
        
        if Receive_flag:
            print(Dict['ip'])
            print(Ip_State[0])
            Ip_List.update(Ip_address)
            if Ip_State[0] == Dict['ip']:
                Device_Id.update(Dict['Values']['Device_Id'])
                Voltage.update(Dict['Values']['Voltage'])
                Up_Current.update(Dict['Values']['Up_Current'])
                Mid_Current.update(Dict['Values']['Mid_Current'])
                Down_Current.update(Dict['Values']['Down_Current'])
                Motor_Status.update(Dict['Values']['Motor_Status'])
                Up_Speed.update(Dict['Values']['Up_Speed'])
                Mid_Speed.update(Dict['Values']['Mid_Speed'])
                Down_Speed.update(Dict['Values']['Down_Speed'])
                Pe_Status.update(Dict['Values']['Pe_Status'])
                Fault.update(Dict['Values']['Fault'])
            Receive_flag = False
    print(str(Ip_address))
    print(str(Ip_Dic))
    if Ip_address:
        Save_Ip_List(str(Ip_address))
    else:
        Save_Ip_List(str(Ip_Dic))
    Window.close()
    print("quit")
    print(len(Data_List))

