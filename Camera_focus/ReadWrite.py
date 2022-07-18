'''
@Descripttion: Null
@version: 1.0
@Author: Mar Ping
@Date: 2020-04-08 16:59:03
LastEditors: Mar Ping
LastEditTime: 2020-11-01 20:46:31
'''
# Read & Write
#UFT-8
import time
import serial
import serial.tools.list_ports

from serial_begin import start_port, find_port

def open_serial(com):
    result = ""
    if (find_port):
        result = start_port(com, 9600, 1)
    #     return start_port(com, 9600, 1)
    # else:
    #     return False
    return result

def stepper_init(port):
    port.write("a".encode())

def stepper_turn(port):
    port.write("b".encode())

def port_close(port):
    port.close()

'''
port = open_serial("COM4")
while(port.readline() != "OK\r\n".encode()):
    stepper_init(port)
    #print(port.readline())

while (1):
    stepper_turn(port)
    time.sleep(0.2)
    if (port.readline() == "END\r\n".encode()):
        break

port_close(port)
'''
