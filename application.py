 ############################# import files ############################
#
from libraries import * 
from loadData import * 
from sagmetation import *
from filters import *
from processing import *
from normalization import *
from dataVisulization  import *
from featureExt  import *
from classifiers  import *

def savedic(dic,filename):
    w = csv.writer(open("/home/goone/results/output."+filename, "w"))
    for key, val in dic.items():
        w.writerow([key, val])

############################# time for application  ##################################
#
start = timeit.default_timer()
#
############################### input parameters  #######################################
#
#
datasetNum = input("input the number of dataset files for program : ")
testNum = input("input the persentage of the test of the data  : ")
testNum = int(testNum)/100
datasetNum = int(datasetNum)
#
#
#####################f######## global variables used  ##################################
##fitered=np.zeros((datasetNum,26,8,36000))
#
#
############################# global variables used  ##################################

path='/home/goone/emg project files/datasets/github datasets/dataset github 2'
#path1='/home/goone/emg project files/datasets/Delsys_8Chans_15Classes(2)/S1-Delsys-15Class'
print("\n num of loaded files : ",datasetNum,'\n')

mat=LoadData(path)

files=mat.fileInpath()
purefiles=mat.browseFiles(files)



matt=mat.inputdata(datasetNum)

ext=mat.extractdata()
labels=ext['mov']

data=mat.conData(matt)
dataPlot(data[0,0,:])  #to (movments*files,channel,samples)

label=mat.loadlabels(labels)

dic=mat.info

############################# ica #######################################


############################# global variables used  ##################################
#
#
#
#hldata1=hlfilter(data,20,400,4) #apply high and low pass filter 
#dataPlot(hldata1[0,0,:])  #to (movments*files,channel,samples)


x=resampleing(data,input_fs=2000,output_fs=1000)
dic['resampling']=list(('2000','1000'))
dataPlot(x[0,0,:])  #to (movments*files,channel,samples)

############################  wavlet dec ##################################
#level=3
#coffnt=wavlet(x)
#y=coffnt[level]
#dic['wavlet level']=list(('2000','200'))
#dataPlot(y[0,5,:])


#filters,waws=filterbanko(data=x,fs=1000)


process=filterbank(20,200,50,20,1000)
bands=process.inputFreqbands()

processdata1,processdata2=process.filterbanko(x)

x1=connTrials(processdata1)
dataPlot(x1[0,0,:])









############################  filteration   ##################################

#ica=Fastica(data)
#icadata=ica.fastica()
#x2=np.array(icadata)

#hldata2=hlfilter(dataRestR2,20,400,5) #apply high and low pass filter 
#dataPlot(hldata1[0,:,:])            #to put the emg into the range of fs 


#nfdata1=notfilter(hldata1)           #apply notch filter to remove the noise
#nfdata2=notfilter(hldata2)           #apply notch filter to remove the noise
#dataPlot(nfdata1[0,:,:])            #at the frequency 50 as defult 

############################ normalization  ##################################

#normdata=norm_mean_std(nfdata)      #apply normalization on data
#dataPlot(normdata[0,5,:])

##
##
############################## classification  ##################################
## wav 500
win=.5
ove=.2
##
dic['sagment data']="window size :"+str(win)+", window  ovelap "+str(ove)
####
####
####y=list()
####for i in range(len(f12)):
y1,z1,c1=conWindow(x1,winSize=win,overSize=ove,fs=200)
labels1=mat.window_lables(label,datasetNum,z1)

#dic['sagment windows bands']=c1[0:z1]

###
############################# feature extraction  ##################################

#featuredata[i]=np.concatenate((r[i],m[i],v[i],p[i],s[i]),axis=0)

#feature_vector=stand(y1)      #,y2,y3,y4,y5,y6)
feature='4'
m=features(y1)

feature_vector=m.conn_Feature(feature=4)
#feature_vector,waw=m.dwt()    #,y2,y3,y4,y5,y6)
dic['features']=feature
#
feature_vector, labels1 = shuffle(feature_vector, labels1, random_state=0)
##
dic['label length']=len(labels1)
##
############################## classification  ##################################
#
x=classification(feature_vector,labels1)

dic['classification accuracy']=accuracy

stop = timeit.default_timer()
print('Time: ', stop - start)  
dic['run time']=stop - start

savedic(dic,'5 500 filterbank 30  ')