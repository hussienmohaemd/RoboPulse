from libraries import * 


def restremov1(data):
    l=list(data.shape)
    s1=int(l[2]/6);s2=2*s1;s3=2*s2;
    p1=int(l[2]/2);p2=int(p1/3);p3=p2*2
    splitedData=np.zeros((l[0],l[1],p1))
    for j in range(l[0]):
        for k in range(l[1]):
            split=np.zeros(int(l[2]/2))
            split[0:p2]=data[j,k,0:s1]
            split[p2:p3]=data[j,k,s2:s2+s1]
            split[p3:p2+p3]=data[j,k,s3:s3+s1]
            splitedData[j,k,:]=split
    
    return splitedData



#def dev_trails(data,trails=3):
#    l=list(data.shape)
#    t1=int(l[2]);t2=int(t1/3);t3=t2*2
#    splitedData1=np.zeros((l[0],l[1],t2))
#    splitedData2=np.zeros((l[0],l[1],t2))
#    splitedData3=np.zeros((l[0],l[1],t2))
#    for i in range(l[0]):
#        for j in range(8):
#            splitedData1[i,j,:]=data[i,j,0:t2]
#            splitedData2[i,j,:]=data[i,j,t2:t3]
#            splitedData3[i,j,:]=data[i,j,t3:t3+t2]    
#    return splitedData1,splitedData2,splitedData3

def dev_trail(data):
    l=list(data.shape)
    t1=int(l[2]);t2=int(t1/6);#t3=t2*2
    splitedData=np.zeros((l[0],l[1],6,t2))
    beg=0; end=t2
    for i in range(l[0]):
        for j in range(8):
            for k in range(6):
                splitedData[i,j,k,:]=data[i,j,beg:end]
                beg+=t2;end+=t2
            beg=0; end=t2
    return splitedData
            
#def connTrial(data,trails=3):
#    z1,z2,z3=dev_trails(data,trails=3)
#    l=list(z1.shape)
#    splitedData=np.zeros((l[0]*trails,l[1],l[2]))
#    for i in range(l[0]):
#        x=i*3
#        splitedData[x]=z1[i]
#        splitedData[x+1]=z2[i]
#        splitedData[x+2]=z3[i]
#    return splitedData


def connTrials(data,trails=6):
    z1=dev_trail(data)
    l=list(z1.shape)
    splitedData=np.zeros((l[0]*l[2],l[1],l[3]))
    x=0
    for i in range(l[0]):
        for j in range(6):
            temp=z1[i,:,j,:]
            splitedData[i+j+x]=temp
        x+=5
    return splitedData

def dev_window(data,winSize=.025, overSize=.01,fs=2000):
#    data=x1
#    winSize=.5;overSize=.1;fs=500
    l=list(data.shape)
    overlap=int(fs*overSize)
    framesize=int(winSize*fs)
    winNum=((l[2]-framesize)/(framesize-overlap)+1)
    if winNum-int(winNum) > 0:
        winNum=int(winNum)+1
    else:
        winNum=int(winNum)
    splitedData1=np.zeros((l[0],l[1],winNum,framesize))
    temp=np.zeros((winNum,framesize))
    begBand=0; endBand=0
    temp1=list()
    for i in range(0,l[0]):
        for j in range(0,l[1]):
            for k in range(0,winNum):
                if k == 0:
                     begBand=0 
                     endBand=framesize
                elif k == winNum-1:
                     begBand=endBand-overlap 
                     endBand=l[2]
                else:
                     begBand=endBand-overlap 
                     endBand=begBand+framesize
                if endBand>=l[2]:
                    endBand=l[2]
                temp3=endBand-begBand
                if k ==winNum-1 or framesize>=temp3:
                    temp[k,0:temp3]=data[i,j,begBand:endBand]

                else:
                    temp[k,:]=data[i,j,begBand:endBand]
                temp1.append((begBand,endBand))
#                temp[k,:]=data[i,j,begBand:endBand]
                splitedData1[i,j,k,:]=temp[k]
    return splitedData1,temp1,winNum
                
                

def conWindow(data,winSize=.025, overSize=.01,fs=500):
    data,band,winnum=dev_window(data,winSize,overSize,fs)
    c=list(data.shape)
    trials=c[0];channels=c[1];winNum=c[2];lenth=c[3]
    splitedData1=np.zeros((trials*winNum,channels,lenth))
    z=0
    for i in range(trials):
        for j in range(channels):
            for k in range(winNum):
                z=i*winNum+k
                splitedData1[z,j,:]=data[i,j,k,:]
    return splitedData1,winNum,band

          