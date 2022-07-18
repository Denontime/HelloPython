'''
@Descripttion: Null
@version: 1.0
@Author: Mar Ping
@Date: 2020-04-07 20:22:08
LastEditors: Mar Ping
LastEditTime: 2020-11-01 13:46:07
'''
import serial
import serial.tools.list_ports


def find_port():
    return list(serial.tools.list_ports.comports())                         
'''
    port_list = list(serial.tools.list_ports.comports())
    if len(port_list) == 0:
        return False
    else:
        return port_list                            
'''



def start_port(ports, speed, timex):  
    ser = serial.Serial()
    ser.port = ports
    ser.baudrate = speed
    ser.timeout = timex
    ser.open()
    return ser
'''
    if find_port() == False:
        return False
    else:
        ser = serial.Serial()
        ser.port = ports
        ser.baudrate = speed
        ser.timeout = timex
        ser.open()

    return ser                                    
'''
