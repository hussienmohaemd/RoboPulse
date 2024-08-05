############################## filtering data #######################################
from libraries import * 

#applying high pass and low path on data
def hlfilter(data,lowfreq=400,highreq=20,order=4,fs=2000):
    x=list(data.shape)
    notchedData=np.zeros((x))
    for i in range (len(data)):
        temp=data[i]
        for j in range (8):
            temp1=temp[j,:]
            emg_correctmean=temp1
            emg_correctmean = temp1 - np.mean(temp1)
            high = 20/(fs*.5)
            low = 400/(fs*.5)
            b, a = sp.signal.butter(order, [high,low], btype='bandpass')
            emg_filtered = sp.signal.filtfilt(b, a, emg_correctmean)                
            notchedData[i,j,:]=emg_filtered
    return notchedData

def notfilter(data,freq=50,qf=30,fs=2000):
    x=list(data.shape)
    notchedData=np.zeros((x))
    for i in range (len(data)):
        temp=data[i]
        for j in range (8):
            temp1=temp[j,:]
            nyq = 0.5 * fs
            noch = freq / nyq
            b, a = scipy.signal.iirnotch(noch, qf)
            notchData = sp.signal.filtfilt(b, a, temp1)
            notchedData[i,j,:]=notchData
    return notchedData

