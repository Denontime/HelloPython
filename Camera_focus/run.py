#from focusing import camera_Open,camera_Close,takePhoto,returnName
from ReadWrite import *
from serial_begin import *
import tkinter as tk
import tkinter.messagebox
import numpy as np
import cv2
import time
import os
import threading

#自定义的线程函数类
def thread_it(func):
    '''将函数放入线程中执行'''
    # 创建线程
    t = threading.Thread(target=func) 
    # 守护线程
    t.setDaemon(True) 
    # 启动线程
    t.start()

def camera_Open():
    cap=cv2.VideoCapture(1)
    return cap

def takePhoto(cap, i):
    ret,frame=cap.read()
    if ret:
        Log.edit_undo()
        cv2.imwrite('./images/' + str(i) + r".png", frame)
        global image_file
        image_file= tk.PhotoImage(file='./images/' + str(i) + r'.png')
        canvas.create_image(328,5,anchor='n', image=image_file)
        canvas.place(x=20,y=15)
        win.update()
        win.after(50)
        Log.insert("insert", './images/' + str(i) + r".png" + '\n')
        
    else:
        return ret

def camera_Close(cap):
    cap.release()

def listDir(path, list_name):  # generate a list of file paths
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        list_name.append(file_path)

def returnName():  #returns the name of the photo with the highest resolution
    path='./images/'   #the path of the photo
    list_name=[]    #list of file paths
    listDir(path,list_name)
    pro_name=os.listdir(path)    #list of all file names
    
    with open('./list.txt','w') as f:   # export list_name to list.txt
        write=''
        file_length=0    #number of statistical files
        for i in list_name:
            write=write+str(i)+'\n'
            file_length=file_length+1
        f.write(write)

    var_list = file_length*['']   #create an empty list of filelength to store the blur of all photos to be detected
    index_i=0    #initializes the index of the photo blur list
    for path in open("list.txt"):    #loop each path in the list
        path = path.replace('\n', '')   #remove line breaks
        img = cv2.imread(path, 1)   #read photos
        width,height = img.shape[:2][::-1]  #set the length and width of the picture
        img_resize = cv2.resize(img,(int(width*1.0),int(height*1.0)),interpolation=cv2.INTER_CUBIC) #input, output picture size, interpolation mode (5 kinds)
        img_gray = cv2.cvtColor(img_resize,cv2.COLOR_RGB2GRAY)  #gray scale
        imageVar = cv2.Laplacian(img_gray, cv2.CV_64F).var()    #image definition
        var_list[index_i]=int(imageVar)   #loop inputs the blur of each image to var_ list
        index_i=index_i+1
    index_j=(var_list.index(max(var_list)))   #output var_ The index corresponding to the maximum clarity in the list
    #print(pro_name[index_j])  #the name of the picture with the highest resolution output
    return pro_name[index_j] #output the clearest picture output


port_rec = {
    "ok": "OK\r\n".encode(),
    "end": "END\r\n".encode()
}

def start():
    Log.insert("insert", 'Starting......................\n')
    cap = camera_Open()
    Log.insert("insert", 'Camera connect!\n')
    port = open_serial(List.get(List.curselection())[0:4])
    Log.insert("insert", 'Serial connect!\n')

    while (port.readline() != port_rec["ok"]):
        time.sleep(1)
        stepper_init(port)  # 初始化
    Log.insert("insert", 'Motor init!\n')

    Log.insert("insert", 'Capture Photo!\n')
    i = 1
    while (i):
        takePhoto(cap, i)
        stepper_turn(port)
        time.sleep(0.1)
        if (port.readline() == port_rec["end"]):
            break
        i = i + 1

    while(port.readline() != port_rec["ok"]):
        time.sleep(1)
        stepper_init(port)  # 初始化
    Log.insert("insert", 'Motor init!\n')

    name = int(returnName()[0:-4]) + 1
    # Log.insert("insert", str(name) + ' site clean!\n')
    for times in range(1,name):
        stepper_turn(port)
        time.sleep(0.1)
        while (port.readline() == ''):
            pass
    takePhoto(cap, 'end')
    Log.insert("insert", str(name) + ' site clean!\n')
    Log.insert("insert", 'Focus complete!\n')



def connection():
    Tip = 'Connection to ' + List.get(List.curselection()) + ' successful!'
    tkinter.messagebox.showinfo(title='Massage', message=Tip)

win = tk.Tk()
win.geometry('1000x720+350+30')
win.iconbitmap('./logo/Analog.ico')
win.title('Camera focus')
#win.overrideredirect(True)
#win.config(background='#87CEEB')

portlist = tk.StringVar()
portlist.set(find_port())

imgBtn1 = tk.PhotoImage(file='./logo/Button1.png')
imgBtn2 = tk.PhotoImage(file='./logo/Button2.png')
Label = tk.PhotoImage(file='./logo/Label.png')
Chose = tk.PhotoImage(file='./logo/Chose.png')

Log = tk.Text(win,
            bd=0,
            #bg='#F0F8FF'
            height=5,
            bg='#87CEEB',
            highlightthickness=5,
            highlightbackground='#AFFEEE',
            highlightcolor='#6495ED',
            undo = True)
Log.place(x=60, y=510)

canvas = tk.Canvas(win,
                bd=3,
                bg='gray',
                height=480,
                width=640)
image_file = tk.PhotoImage(file='./logo/BG.png')
canvas.create_image(328,0,anchor='n', image=image_file)
canvas.place(x=20,y=15)

Port = tk.Label(win, image=Label)
Port.place(x=675,y=30)
List = tk.Listbox(win,
                font=('Microsoft YaHei UI', 14),
                bg='#ADD8E6',
                borderwidth=0,
                selectbackground='#1E90FF',
                highlightthickness=5,
                highlightbackground='#AFFEEE',
                highlightcolor='#6495ED',
                selectborderwidth=0,
                relief='flat',
                listvariable=portlist)
List.place(x=725,y=150)

Enter = tk.Button(win,image=Chose, bd=0, command=connection)
Enter.place(x=750,y=450)

Start = tk.Button(win, bd=0, image=imgBtn1, command=lambda :thread_it(start))
Start.place(x=40,y=600)

Exit = tk.Button ( win, bd=0,image=imgBtn2, command=win.destroy)
Exit.place(x=410,y=600)

win.mainloop()  # 进入消息循环

