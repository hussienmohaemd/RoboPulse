from libraries import *


class LoadData:
    """loaddata class for loading dataset file (csv , .mat).
    """

    def __init__(self,path,filetype='mat'):
        """Initialize the Butterworth bandpass filter.
        Arguments:
            path (string): path for the dataset
            filetype (string): the type of loaded file
            filenum (int): the num of loaded file
            fs (int): sampling frequency
        """
        self.path = path
        self.filetype = filetype
        self.file=""
        self.info={}
#        self.filenum=1

  


    
    def loadcsv(self,filesnum):
        files=LoadData.fileInpath(self)
        files2=LoadData.browseFiles(self,files)
        pas=list()
        s=self.path+'/'
        for i in range(len(files2)):
            pas.append(s+files2[i])
        data=list()
        rowdata = pd.read_csv(pas[filesnum],error_bad_lines=False)
        data.append(rowdata)
        return data
        
        
    def extracto(file):
        x=file.dtype
        y=str(x)
        x=y.replace("O","")
        y=x.replace("[","")
        x=y.replace("]","")
        y=x.replace("(","")
        x=y.replace(")","")
        y=x.replace("'","")
        x=y.replace(" ","")
        y=x.replace(",","=")
        x=y.split("=")
        for i in x:
            if i=='':
                x.remove(i)
        matfile={}
        for i in x:
            tmp=file[i]
            tmp=tmp[0].tolist()
            tmp=tmp[0]
    #        tmp=tmp[0]
            matfile[i]=tmp
        return matfile


        
    
    
    def fileInpath(self):
        files=os.listdir(self.path)
        self.info['dataPath']=self.path
        return files
    
    def browseFiles(self,files):
        file=list()
        for i in range (len(files)):
            if ".mat"  in files[i]:
                file.append(files[i])
            if  ".csv" in files[i] :
                file.append(files[i])
    
        file=natsorted(file)#,reverse=False
        self.file=file
        self.info['dataFiles']=self.file
        return self.file

    
#    def extractFile(self,numload=1):
#        tmp=0
#        for i in range(len(self.file)):
#            if ".csv" in self.file[i]:
#                tmp=0
#                break
#        if tmp==0:
#            x=LoadData.loadcsv(self,numload)
#        else:
#            x=LoadData.loadFilemat(self,numload)
#
#        return x
#    
        
    def extractdata(self,filenum=0):
        if ".mat" in self.file[0]:
            x=LoadData.loadFilemat(self,filenum)
            self.info['dataType']=".mat"
        else:
            x=LoadData.loadcsv(self,filenum)
            self.info['dataType']=".csv"
        return x
    
    def loadFilemat1(self,filesnum=1):
        files=LoadData.fileInpath(self)
        files2=LoadData.browseFiles(self,files)
        pas=list()
        s=self.path+'/'
        for i in range(len(files2)):
            pas.append(s+files2[i])
        tmp = scipy.io.loadmat(pas[filesnum])
        return tmp
    
    
    def loadFilemat(self,filesnum=1,alarm=False):
        files=LoadData.fileInpath(self)
        files2=LoadData.browseFiles(self,files)
        pas=list()
        s=self.path+'/'
        for i in range(len(files2)):
            pas.append(s+files2[i])
        tmp = scipy.io.loadmat(pas[filesnum])
        if alarm:
            return tmp
        s=sorted(tmp.keys())
        x=['__globals__', '__header__', '__version__']
        for i in range(len(s)):
            if s[i] not in x:
                c=s[i]
        temp=tmp[c]
        temp=LoadData.extracto(temp)
        return temp
    
    def palancedata(self,data):
        temp=list()
        if self.filetype=='mat':
            for i in range(len(data)):
                temp.append((data[i].T))
            temp=np.array(temp)
        else:
            for i in range(len(data)):
                temp.append((data[i][0].T).values)
        return temp
    
    def inputdata(self,filenum,datas='tdata'):
        data=list()
        self.info['dataLoaded']=filenum
        for i in range(filenum): 
            if self.filetype=='mat':
                x=LoadData.loadFilemat(self,filesnum=i)
                tmp=x[datas]
                data.append(tmp)
            elif self.filetype=='csv':
                x=LoadData.loadcsv(self,filesnum=i)
                data.append(x)
        if self.filetype=='mat':
            data=LoadData.palancedata(self,data)
        return data


################# loadlabels and labels process ########################



    def loadlabels(self,file):
        file=file.tolist()
        for i in range(len(file)):
            file[i]=str(file[i][0][0])
        return file
            
    
    
    def trial_labels(self,label,num1,trials=3,y='rest'):
        labels=label*num1 # labels * num of file,ys loaded
        result=list()
        for i in range (len(labels)):  # iteration on label
            a=labels[i] 
            for j in range(trials):
                result.append(a)
                result.append(y)
        return result
    
    def window_lables(self,label,num,num2=1,trials=3):
        labels=LoadData.trial_labels(self,label,num,trials=3)
        x=list()
        k=0
        for i in range(len(labels)*num2):
            if (i) % num2==0 and i!=0:
                k+=1
            x.append((labels[k]))
            if k==len(labels):
                return x
        return x

    def conData(self,data):
        l=len(data)
        x=data[0]
        for i in range(1,l):
            x=np.concatenate((x, data[i]), axis=0)
        return x
   