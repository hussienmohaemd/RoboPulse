from libraries import * 


#
#def wavlet(data,levelnum=4,wafmoth='db4'):
#    coeffs = wavedec(data, wafmoth, level=levelnum)
#    return coeffs
#
#
#
############################ filter bank ###################################
#
#
#def filterbank(data,freq_band=[[50,100],[80,130],[110,160],[140,190],[170,220],[200,250]],fs=500):
#    
#    
##    data=dataRestR1
##    l=data.shape
##    ll=len(freq_band)
#    temp=list()
#    filResult = None
#    nquest=fs*0.5
#    for freqs in freq_band:
#        
#        if len(freqs) == 1:
#            b, a = butter(4, freqs[0] / nquest, btype='lowpass')
#        else:
#            freqs=freq_band[0]
#            freqs = [x / nquest for x in freqs]
#            b, a = butter(4, np.array(freqs), btype='bandpass')
#        data_filtered = sp.signal.filtfilt(b, a, data)
##        filResult = data_filtered if filResult is None else np.c_[filResult, data_filtered]
#        temp.append(data_filtered)
#    return temp
#
#def filterbanko(data,freq_band=[[50,70],[60,80],[70,90],[80,100],[90,110],[100,120],[110,130],[120,140],[130,150],[140,160],[150,170],[160,180],[170,190],[180,200]],fs=2000):
##    data=x
##    fs=200
##    l=data.shape
##    ll=len(freq_band)
#    temp=list()
#    filResult = None
#    nquest=fs*0.5
#    i=0
#    for freqs in freq_band :
#
#        freqs=freq_band[0]
#        freqs = [x / nquest for x in freqs]
#        b, a = butter(4, np.array(freqs), btype='bandpass')
#        data_filtered = sp.signal.filtfilt(b, a, data)
#        if i==0:
#            filResult=data_filtered
#        else:
#            np.c_[filResult, data_filtered]
#        temp.append(data_filtered)
#        i+=1
#
#    return filResult,temp
#
#
#class Fastica:
#    
#    def __init__(self,data,compon=250):
#        self.data=data
#        self.compon=compon
#    
#    def fastica(self):
#        temp=list()
#        for i in range(len(data)):
#            transformer = FastICA(n_components=self.compon,random_state=0)
#            X_transformed = transformer.fit_transform(self.data[i,:,:])
#            temp.append(X_transformed)
#        return temp
#    
    

class wavletdec:

    """ButterBandpass class for apply bandpass filter on data."""

    def __init__(self,level=4,fs=1000,wafmoth='db4'):
        """ButterBandpass filter parameters.
        Arguments:
            level (string): path for the dataset
            wafmoth (string): the type of loaded file
            fs (int): sampling frequency
        """
        self.level = level
        self.wafmoth = wafmoth
        
    
    def wavlet(self,data):
        coeffs = wavedec(data, self.wafmoth, level=self.level)
        return coeffs
    
    
class filterbank:
    
    """ButterBandpass class for apply bandpass filter on data."""
        
    def __init__(self,bandBeg,bandEnd,bandSize,bandOverlap,fs=1000,level=4):
        """ButterBandpass filter parameters.
        Arguments:
            bandBeg (string): path for the dataset
            bandEnd (string): the type of loaded file
            bandSize (string): path for the dataset
            bandOverlap (string): the type of loaded file
            fs (int): sampling frequency
            level (int): sampling frequency

        """
        self.bandBeg = bandBeg
        self.bandEnd = bandEnd
        self.bandSize = bandSize
        self.bandOverlap = bandOverlap
        self.fs = fs
        self.level = level


    def inputFreqbands(self):
       lenth=self.bandEnd-self.bandBeg
       winNum=((lenth-self.bandSize)/(self.bandSize-self.bandOverlap)+1)
       if winNum-int(winNum) > 0:
            winNum=int(winNum)+1
       else:
            winNum=int(winNum)
       x=self.bandBeg;y=self.bandBeg+self.bandSize
       temp1=list()
       for i in range(winNum):
           temp1.append((list((x,y))))
           x=x+self.bandSize-self.bandOverlap
           y=x+self.bandSize
       return temp1
    
        
    
    def filterbanko(self,data):
        freq_band=filterbank.inputFreqbands(self)
        temp=list()
        filResult = None
        nquest=self.fs*0.5
        i=0
        for freqs in freq_band :
    
            freqs=freq_band[0]
            freqs = [x / nquest for x in freqs]
            b, a = butter(self.level, np.array(freqs), btype='bandpass')
            data_filtered = sp.signal.filtfilt(b, a, data)
            if i==0:
                filResult=data_filtered
            else:
                np.c_[filResult, data_filtered]
            temp.append(data_filtered)
            i+=1
        return filResult,temp
