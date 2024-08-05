from libraries import * 

#####################    data visualization       ###################################

def dataPlot(data,fs=2000,x='/home/elgamal/www/'):
    dataLen=max(data.shape)
    time = np.array([i/fs for i in range(0, dataLen, 1)]) # sampling rate 2000 Hz
    fig = plt.figure()
    plt.plot(time, data.T)
    plt.xlabel('Time (sec)')
    plt.ylabel('EMG (a.u.)')
#    plt.savefig(x+'.png')
    fig.set_size_inches(w=11,h=7)


    