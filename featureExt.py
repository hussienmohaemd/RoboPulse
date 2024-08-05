from libraries import * 


################################ features ############################################

class features:
    
    def __init__(self,data):
        self.data=data

    def rms(self):
        l=list(self.data.shape)
        rmsdata=np.zeros((l[0],l[1]))
        for i in range(l[0]):
            for j in range(l[1]):
                rmsdata[i,j]=np.sqrt(np.mean(np.square(self.data[i,j,:])))
            
        return rmsdata
     
    
    def mav(self):
        l=list(self.data.shape)
        mavdata=np.zeros((l[0],l[1]))
        for i in range(l[0]):
            for j in range(l[1]):
                mavdata[i,j]=np.mean(np.abs(self.data[i,j,:])) 
        return mavdata
    
    def dimReduction(self):
        l=list(self.data.shape)
        mavdata=np.zeros((l[0]))
        for i in range(l[0]):
                mavdata[i]=np.mean(self.data[i,:]) 
        return mavdata
    
    def var(self):
        l=list(self.data.shape)
        vardata=np.zeros((l[0],l[1]))
        for i in range(l[0]):
            for j in range(l[1]):
                vardata[i,j]=np.log10(np.var(self.data[i,j,:]))
        return vardata
    
    
    def power(self):
        l=list(self.data.shape)
        powdata=np.zeros((l[0],l[1]))
        for i in range(l[0]):
            for j in range(l[1]):
                powdata[i,j]=np.power(self.data[i,j,:], 2).mean(axis=0)
        return powdata
    
    def stand(self):
        l=list(self.data.shape)
        stdfata=np.zeros((l[0],l[1]))
        for i in range(l[0]):
            for j in range(l[1]):
                stdfata[i,j]=np.std(self.data[i,j,:])
        return stdfata
    
    def dwt(self):
        l=list(self.data.shape)
        dwtdata=np.zeros((l[0],l[1]))
        for i in range(l[0]):
            for j in range(l[1]):
                	dwtdata[i,j] = pywt.dwt(self.data[i,j,:], 'db4')
        return dwtdata
    
    
    def meaan(self):
        l=list(self.data.shape)
        meandata=np.zeros((l[0],l[1]))
        for i in range(l[0]):
            for j in range(l[1]):
                meandata[i,j]=np.mean(self.data[i,j,:])
        return meandata
    
    
    #def wl(data):
    #    l=list(data.shape)
    #    wavlength=np.zeros((l[0],l[1]))
    #    for i in range(l[0]):
    #        for j in range(l[1]):
    #            wavlength[i,j]=np.sum(np.absolute(np.diff(data[i,j,:], axis=0)), axis=0)
    #    return wavlength
        
    
    def poower(self):
        l=list(self.data.shape)
        powwer=np.zeros((l[0],l[1]))
        for i in range(l[0]):
            for j in range(l[1]):
                f=np.fft.fft(self.data[i,j,:])
                P=f * np.conjugate(f)
                powwer[i,j] = sum(P)
        return powwer
    
    
#    def coherence(self):
#        l=list(self.data.shape)
#        fs=500
#        meandata=np.zeros((l[0],l[1]))
#        for i in range(l[0]):
#            for j in range(l[1]):
#                b, a = signal.butter(2, 0.25, 'low')
#                y = signal.lfilter(b, a, self.data[i,j,:])
#                meandata[i,j], Cxy = signal.coherence(self.data[i,j,:], y, fs)
#        return f,Cxy
    
    
#    def selectFeature(self,x):
#        r=0
#        if x == 'rms':
#            r=features.rms(self);
#        elif x == 'mav':
#            r=features.mav(self)
#        elif x == 'var':
#            r=features.var(self);
#        elif x == 'mean':
#            r=features.meaan(self);
#        elif x == 'stand':
#            r=features.stand(self);
#        elif x == 'power':
#            r=features.power(self);
##        elif x == 'coh':
##            r=features.coherence(self)
#        elif x == 'power2':
#            r=features.poower(self)
#        elif x == 'dwt':
#            r=features.dwt(self)
#        return r
#    
    
    def conn_Feature(self,feature=2):
        l=list(self.data.shape)
        featuredata=np.zeros((l[0],l[1]*feature))
        r=features.rms(self);p=features.power(self);
        m=features.mav(self);s=features.stand(self);
        v=features.var(self);me=features.meaan(self);
        for i in range(len(self.data)):
            if feature==2:
                featuredata[i]=np.concatenate((s[i],v[i]),axis=0)
            elif feature==3:
                featuredata[i]=np.concatenate((s[i],v[i],me[i]),axis=0)
            elif feature==4:
                featuredata[i]=np.concatenate((r[i],m[i],v[i],s[i]),axis=0)
            elif feature==5:
                featuredata[i]=np.concatenate((r[i],m[i],v[i],s[i],p[i]),axis=0)
            elif feature==6:
                featuredata[i]=np.concatenate((r[i],m[i],v[i],p[i],s[i],me[i]),axis=0)
        return featuredata

