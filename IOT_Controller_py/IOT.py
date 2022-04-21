'''
Descripttion: Null
version: 1.0
Author: Mar Ping
Date: 2021-03-18 11:50:11
LastEditors: Mar Ping
LastEditTime: 2021-03-28 21:35:47
'''
import binascii
import os
import random
import socket  # 导入socket模块
import sys
import threading
import time  # 导入time模块

from matplotlib.backends.backend_tkagg import (FigureCanvasAgg,FigureCanvasTkAgg)
from matplotlib.figure import Figure

import PySimpleGUI as sg

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
            log.writelines(str(Dict) + '\n')



STEP_SIZE = 1
SAMPLES = 10000
SAMPLE_MAX = 5500
CANVAS0_SIZE = (1250, 300)
CANVAS_SIZE = (400, 300)

def draw_figure(canvas, figure, loc=(0, 0)):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg

def DifferentScales():
    import matplotlib.pyplot as plt
    import numpy as np

    # Create some mock data
    t = np.arange(0.01, 10.0, 0.01)
    data1 = np.exp(t)
    data2 = np.sin(2 * np.pi * t)

    fig, ax1 = plt.subplots()

    color = 'tab:red'
    ax1.set_xlabel('time (s)')
    ax1.set_ylabel('exp', color=color)
    ax1.plot(t, data1, color=color)
    ax1.tick_params(axis='y', labelcolor=color)

    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

    color = 'tab:blue'
    ax2.set_ylabel('sin', color=color)  # we already handled the x-label with ax1
    ax2.plot(t, data2, color=color)
    ax2.tick_params(axis='y', labelcolor=color)

    fig.tight_layout()  # otherwise the right y-label is slightly clipped
    return fig

def Ui():
    sg.theme('BrownBlue')
    Frame_Left_Layout = sg.Frame("Left", [[sg.Column([[sg.Listbox(Ip_address, key='-IP-LIST-', size=(16, 15))],
                                                    [sg.Button("Connect"), sg.Exit()]],
                                                    size=(150,700), element_justification='center')]]
    )
    Frame0 = sg.Frame("Voltage",[[ sg.Graph(CANVAS0_SIZE, (0, 0), (SAMPLES, SAMPLE_MAX),
                                background_color='black', key='graph0')]])
    Frame1 = sg.Frame("UP_Motor",[[ sg.Graph(CANVAS_SIZE, (0, 0), (SAMPLES, SAMPLE_MAX),
                                background_color='black', key='graph1')]])
    Frame2 = sg.Frame("Mid_Motor",[[ sg.Graph(CANVAS_SIZE, (0, 0), (SAMPLES, SAMPLE_MAX),
                                background_color='black', key='graph2')]])
    Frame3 = sg.Frame("Down_Motor",[[ sg.Graph(CANVAS_SIZE, (0, 0), (SAMPLES, SAMPLE_MAX),
                                background_color='black', key='graph3')]])
    Frame_Right_Layout = sg.Frame("Right", [[Frame0], [Frame1, Frame2, Frame3]])
    layout = [[Frame_Left_Layout,Frame_Right_Layout]]
    Window = sg.Window("IOT", layout, finalize=True)
    
    return Window

if __name__ == '__main__':
    Ip_Dic = eval(Get_Ip_List())
    print(Ip_Dic)
    my_thread = threading.Thread(target=Socket)
    Window = Ui()
    my_thread.setDaemon(True)
    my_thread.start()
    
    Ip_List = Window['-IP-LIST-']
    Ip_List.update(Ip_Dic)
    
    V_canvas = Window["graph0"]
    Up_canvas = Window["graph1"].TKCanvas
    Mid_canvas = Window["graph2"].TKCanvas
    Down_canvas = Window["graph3"].TKCanvas

    V_canvas.draw_line((SAMPLES//2, 0), (SAMPLES//2,SAMPLE_MAX),color='yellow')
    V_canvas.draw_line((0,SAMPLE_MAX//2), (SAMPLES, SAMPLE_MAX//2),color='red')

    #/**************************************  *************************************/
    fig = Figure(figsize=(4,3))
    ax = fig.add_subplot(111)
    ax.set_xlabel("X axis")
    ax.set_ylabel("Y axis")
    ax.grid()
    Fig_Up = draw_figure(Up_canvas, fig)
    Fig_Mid = draw_figure(Mid_canvas, fig)
    Fig_Down = draw_figure(Down_canvas, fig)
    #/**************************************  *************************************/

    prev_response_time = None
    i = 0
    prev_x, prev_y = 0, 0
    graph_value = 2000
    figures = []
    data_points = 40 #/***************************
    while True:
        event, values = Window.read(timeout=0)
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
    #/**************************************  *************************************/
        # slider_elem.update(i)       # slider shows "progress" through the data points
        ax.cla()                    # clear the subplot
        ax.grid()                   # draw the grid
        # data_points = int(values['-SLIDER-DATAPOINTS-']) # draw this many data points (on next line)
        #ax.plot(range(data_points), Data_List[Data_List_Index]['Values']['Up_Speed'], color='purple')    //////////////////
        Fig_Up.draw()
        Fig_Mid.draw()
        Fig_Down.draw()
    #/**************************************  *************************************/

        # graph_offset = random.randint(-10, 10)
        # graph_value = graph_value + graph_offset

        # if graph_value > SAMPLE_MAX:
        #     graph_value = SAMPLE_MAX
        # if graph_value < 0:
        #     graph_value = 0

        # new_x, new_y = i, graph_value
        # prev_value = graph_value

        # if i >= SAMPLES:
        #     V_canvas.delete_figure(figures[0])
        #     figures = figures[1:]
        #     for count, figure in enumerate(figures):
        #         V_canvas.move_figure(figure, -STEP_SIZE, 0)
        #     prev_x = prev_x - STEP_SIZE

        # last_figure = V_canvas.draw_line((prev_x, prev_y), (new_x, new_y), color='white')
        # figures.append(last_figure)
        # prev_x, prev_y = new_x, new_y
        # i += STEP_SIZE if i < SAMPLES else 0

    Window.close()


