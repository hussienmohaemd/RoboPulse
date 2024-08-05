 ############################# import files ############################
from libraries import * 
from loadData import * 
from sagmetation import *
from filters import *
from processing import *
from normalization import *
from dataVisulization  import *
from featureExt  import *
from classifiers  import *


############################ time for application  ##################################

start = timeit.default_timer()

############################## input parameters  #######################################


datasetNum = input("input the number of dataset files for program : ")
testNum = input("input the persentage of the test of the data  : ")
testNum = int(testNum)/100
datasetNum = int(datasetNum)


####################f######## global variables used  ##################################
fitered=np.zeros((datasetNum,26,8,36000))


############################ global variables used  ##################################


labels1=pre_labels(label,datasetNum)


print("\n num of loaded files : ",datasetNum,'\n')
print("length of labels : ",np.shape(labels1),'\n')

matt=input_data(datasetNum)
print("num of database file loaded :",matt.shape,'\n')

print("duration of the data for window spliting : ",18000/1000,"s",'\n')


############################ global variables used  ##################################


movData=conData(matt)       #reducde data from (files,movments,channels,samples)
dataPlot(movData[0,:,:])  #to (movments*files,channel,samples)


############################  wavlet dec ##################################


#coffnt=wavlet(movData,4)
#wavdata1=coffnt[3]
#wavdata2=coffnt[2]
#dataPlot(wavdata2[0,5,:])


############################ remove the rest period between trials ##################################

dataRestR1=restremov1(movData) #remove the rest period between trials
dataPlot(dataRestR1[0,:,:])
############################  filteration   ##################################


#hldata1=hlfilter(dataRestR1,20,400,5) #apply high and low pass filter 
#hldata2=hlfilter(dataRestR2,20,400,5) #apply high and low pass filter 
#dataPlot(hldata1[0,:,:])            #to put the emg into the range of fs 


#nfdata1=notfilter(hldata1)           #apply notch filter to remove the noise
#nfdata2=notfilter(hldata2)           #apply notch filter to remove the noise
#dataPlot(nfdata1[0,:,:])            #at the frequency 50 as defult 

############################ normalization  ##################################

#normdata=norm_mean_std(nfdata)      #apply normalization on data
#dataPlot(normdata[0,5,:])

#noradata=norm_min_max(nfdata)                     
#dataPlot(noradata[0,:,:])

############################ split date into trials  ##################################

x1=connTrial(dataRestR1,trails=3)
dataPlot(x1[0,5,:])





############################ sagmentation into window  ##################################

#win=.5
#ove=.1
#y1,z1,c1=conWindow(x1,winSize=win,overSize=ove,fs=2000)
##y2,z2,c2=conWindow(x2,winSize=win,overSize=ove,fs=250)
#labels22=pre_labels(label,datasetNum,z1)

############################ processing using filterbank ##################################

f1,f2=filterbank(x1,fs=2000)

#np.save('/home/goone/projects /variable files/flterbank12', f2)
#f2 = np.load('/home/goone/projects /variable files/flterbank12.npy')

############################ feature extraction  ##################################

feature_vector=conn_Feature(f2[0],f2[1],f2[2],f2[3])

feature_vector, labels1 = shuffle(feature_vector, labels1, random_state=0)


############################ classification  ##################################

x=classification(feature_vector,labels1)

stop = timeit.default_timer()
print('Time: ', stop - start)  