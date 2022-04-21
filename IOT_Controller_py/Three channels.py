import socket
import numpy as np
import matplotlib.pyplot as plt
import threading

UdpClient = None
cacheCount=500
topLimit_y=6000

lowLimit_y=0
#topLimit_y=6000
#lowLimit_y=1500
interval_y=200

x=cacheCount
speed_list_1 = list(np.zeros(cacheCount,))
speed_list_2 = list(np.zeros(cacheCount,))
speed_list_3 = list(np.zeros(cacheCount,))

def receiveData():
    global UdpClient,x,speed_list_1,speed_list_2,speed_list_3
    while True:
        data = UdpClient.recv(1024)
        #print("here2")
        data = data.hex()

        #data = int(data[0:4], 16)
        #print(data)
        speed_list_1.append(int(data[0:4], 16))
        speed_list_2.append(int(data[4:8], 16))
        speed_list_3.append(int(data[8:12], 16))
        x+=1
        



if __name__ == '__main__':
    IP = "192.168.10.110"
    Port = 8881

    UdpClient = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    UdpClient.bind((IP, Port))
    UdpClient.settimeout(100)

    plt.figure(figsize=((10, 6)))
    # plt.figure()
    #plt.axis([0, cacheCount, 3000, 4500])
    plt.grid(axis="y")
    thread_new=threading.Thread(target=receiveData)
    thread_new.start()
    #print("here")
    plt.ion()
    
    plt.yticks(range(3000, 4500, 50))
   
    # plt.xlim(0, 1000)
    while True:
        pass
        # plt.plot(range(x), speed_list)
        plt.pause(0.02)
        # # 100为一周期
        if x > cacheCount:
            #x -= 1
            #del speed_list[0]
            #plt.xticks(range(x-1000,x, 200))
            #plt.xticks(range(x-cacheCount, x, 50))
            plt.clf()
            plt.plot(range(x-cacheCount,x), speed_list_1[-cacheCount:],'r-')
            plt.plot(range(x-cacheCount,x), speed_list_2[-cacheCount:],'g-')
            plt.plot(range(x-cacheCount,x), speed_list_3[-cacheCount:],'b-')
            plt.yticks(range(lowLimit_y, topLimit_y, interval_y))
            plt.xticks(range(x-500, x, 25))
            # plt.axis([0,1000,0,200])
           # plt.yticks(range(0, 400, 20))
            
        else:
            pass
            #plt.xticks(range(0, x, 10))
            #plt.plot(range(x), speed_list_1,'r-')
            #plt.plot(range(x), speed_list_2,'g-')
            #plt.plot(range(x), speed_list_3,'b-')
            #plt.yticks(range(lowLimit_y, topLimit_y, interval_y))
            #plt.yticks(range(4000, 4500, 20))


        

