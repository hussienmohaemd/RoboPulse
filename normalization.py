from libraries import * 


##############################  data normilization #################################
#data normilizations
def norm_mean_std(data):
    x=list(data.shape)
    notchedData=np.zeros((x))
    for i in range (len(data)):
        temp=data[i]
        for j in range (8):
            temp1=temp[j,:]
            mean = np.mean(temp1, axis=0)
            std_dev = np.std(temp1, axis=0)
            notchedData[i,j,:]= (temp1 - mean) / std_dev
    return notchedData


#data normilizations
def norm_min_max(data):
    x=list(data.shape)
    notchedData=np.zeros((x))
    for i in range (len(data)):
        temp=data[i]
        for j in range (8):
            temp1=temp[j,:]
            notchedData[i,j,:]=  (temp1 - np.min(temp1))/(np.max(temp1)-np.min(temp1))
    return notchedData


def resample_by_interpolation(signal, input_fs, output_fs):
    scale = output_fs / input_fs
    # calculate new length of sample
    n = round(len(signal) * scale)
    resampled_signal = np.interp(
        np.linspace(0.0, 1.0, n, endpoint=False),  # where to interpret
        np.linspace(0.0, 1.0, len(signal), endpoint=False),  # known positions
        signal,  # known data points
    )
    return resampled_signal

def resampleing(data, input_fs=2000, output_fs=500):
    l=list(data.shape)
    scale = output_fs/input_fs
    n = round(l[2] * scale)
    temp=np.zeros((l[0],l[1],n))
    for i in range(l[0]):
        for j in range(l[1]):
            temp[i,j,:]=resample_by_interpolation(data[i,j,:], input_fs, output_fs)
    return temp

    

#def compare(signal, input_fs, output_fs):
#
#    x = np.linspace(0, 10, 256, endpoint=False)
#    y =signal
#    yre = scipy.signal.resample(y,20)
#    xre = np.linspace(0, 10, len(yre), endpoint=False)
#    
#    yre_polyphase = scipy.signal.resample_poly(y, 20, 256)
#    yre_interpolation = resample_by_interpolation(y, 256, 20)
#    
#    plt.figure(figsize=(10, 6))
#    plt.plot(x,y,'b', xre,yre,'or-')
#    plt.plot(xre, yre_polyphase, 'og-')
#    plt.plot(xre, yre_interpolation, 'ok-')
#    plt.legend(['original signal', 'scipy.signal.resample', 'scipy.signal.resample_poly', 'interpolation method'], loc='lower left')
#    plt.show()    