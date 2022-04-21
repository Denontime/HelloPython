import socket
import numpy as np
import matplotlib.pyplot as plt
import threading

UdpClient = None
cacheCount=500
topLimit_y=5300
lowLimit_y=3400
interval_y=50
x=cacheCount
speed_list = list(np.zeros(cacheCount,))

def receiveData():
    global UdpClient,x,speed_list
    while True:
        data = UdpClient.recv(1024)
        #print("here2")
        data = data.hex()
        data = int(data, 16)
        print(data)
        speed_list.append(data)
        x+=1
        



if __name__ == '__main__':
    IP = "192.168.10.110"
    Port = 8881

    UdpClient = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    UdpClient.bind((IP, Port))
    UdpClient.settimeout(100)

    plt.figure(figsize=((10, 6)))
    # plt.figure()
    plt.axis([0, 201, 3000, 4500])
    plt.grid(axis="y")
    thread_new=threading.Thread(target=receiveData)
    thread_new.start()
    #print("here")
    plt.ion()
    
    plt.yticks(range(3000, 4500, 50))
    while True:
        pass
        

        # plt.plot(range(x), speed_list)

        
        plt.pause(0.02)
        plt.cla()
        
        
        # # 100为一周期
        if x > cacheCount:
            #x -= 1
            #del speed_list[0]
            #plt.xticks(range(x-200,x, 10))
            plt.xticks(range(x-cacheCount, x, 15))
            plt.plot(range(x-cacheCount,x), speed_list[-cacheCount:])
            plt.yticks(range(lowLimit_y, topLimit_y, interval_y))
            #plt.yticks(range(4000, 4500, 20))
            
        else:
            plt.xticks(range(0, x, 10))
            plt.plot(range(x), speed_list)
            plt.yticks(range(lowLimit_y, topLimit_y, interval_y))
            #plt.yticks(range(4000, 4500, 20))


        

