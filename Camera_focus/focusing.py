'''
Descripttion: Null
version: 1.0
Author: Mar Ping
Date: 2020-10-24 17:21:28
LastEditors: Mar Ping
LastEditTime: 2020-11-01 13:49:07
'''
import numpy as np
import cv2
import os
import time

def camera_Open():
    cap=cv2.VideoCapture(0)
    return cap

def takePhoto(cap, i):
    ret,frame=cap.read()
    if ret:
        cv2.imwrite('./images/' + str(i) + r".png", frame)
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
    print(pro_name[index_j])  #the name of the picture with the highest resolution output
    return pro_name[index_j] #output the clearest picture output



