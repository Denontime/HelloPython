#米勒编码
import matplotlib.pyplot as plt
import numpy as np
N=8 #码元数
a=128#采样次数
n=a*N
x=np.linspace(0,N,n)
y=np.linspace(0,N,n)          #x,y对应的采样点数目
last=1                          #上一个码元的后半部分值,设置初值为1
RAN0=1                          #上一个随机信号,设置初值为1
list1=[1,0,1,1,0,0,1,0]
for i in range(N):
    RAN=int(list1[i])#生成0-1之间的随机浮点数,并且四舍五入
    b=i*a
    if RAN==1:                          #当输入信号为1
        for j in range(a):
            if j in range(64):          #米勒编码码元中间跳变表示的是1
                y[b+j]=last           #前半部分赋值为上一个码元后半部分的值
            else:
                y[b+j]=abs(last-1)      #后半部分赋值为跳变后的值
        last=abs(last-1)            #last的值改变
    else:                           #当输入信号为0 米勒编码中间不跳变表示0
        if RAN0==0:                     
            for j in range(a):  
                y[b+j]=abs(last-1)  #如果为连续0 码元开始时跳变，所有采样点赋值为跳变后的值
            last=abs(last-1)        #last的值改变
        else:
            for j in range(a):      #如果为单个0 码元的所有采样点赋值为上一个码元的后半部分的值
                y[b+j]=last
    RAN0=RAN
    print(RAN)              #为了方便检验输出波形是否正确
plt.xlim(0,N)
plt.ylim(-1,2)                        #x,y轴的范围
plt.xticks(np.arange(0,N,1),np.arange(0,N,1))       #设置x轴间隔和标签      
plt.title("Miller")                        #设置标题
plt.plot(x,y,color='r',linewidth=1,linestyle="-")   #绘制波形
plt.show()
