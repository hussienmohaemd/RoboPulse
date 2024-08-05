from libraries import * 
from sklearn.linear_model import LogisticRegression
accuracy={}




################################## svm ################################
def svmcl(feature_vector,labels22,testNum=.3):
    X_train, X_test, y_train, y_test = train_test_split(feature_vector, labels22, test_size=testNum, random_state=0)

    svvm = svm.SVC(kernel='linear')
    score1 = cross_val_score(svvm, feature_vector, labels22, cv=5)
    accuracy.update({'svm with cross validation':score1.mean()*100})
    end=svvm.fit(X_train,y_train)
    y_pred=svvm.predict(X_test)
    accuracy.update({'svm':metrics.accuracy_score(y_test, y_pred)*100})
    

############################################# knn ##################################
def knncl(feature_vector,labels22,testNum=.3):
    X_train, X_test, y_train, y_test = train_test_split(feature_vector, labels22, test_size=testNum, random_state=0)

    
    knn = KNeighborsClassifier(n_neighbors=6)
    
    score2 = cross_val_score(knn, feature_vector, labels22, cv=5)
    accuracy.update({'knn  with cross validation ':score2.mean()*100})
    knn.fit(X_train,y_train)
    y_pred=knn.predict(X_test)
    accuracy.update({'knn':metrics.accuracy_score(y_test, y_pred)*100})

################################### cnn #############################################
def mlpcl(feature_vector,labels22,testNum=.3):
    X_train, X_test, y_train, y_test = train_test_split(feature_vector, labels22, test_size=testNum, random_state=0)

    mlp = MLPClassifier(hidden_layer_sizes=(30,), max_iter=800, alpha=1e-4,
                        solver='sgd', verbose=10, tol=1e-4, random_state=1,
                        learning_rate_init=.1)
    
    score3 = cross_val_score(mlp, feature_vector, labels22, cv=5)
    accuracy.update({'multi layer perceptron with cross validation ':score3.mean()*100})
    mlp.fit(X_train,y_train)
    y_pred=mlp.predict(X_test)
    accuracy.update({'multi layer perceptron':metrics.accuracy_score(y_test, y_pred)*100})

#################################  lda ###############################################
def ldacl(feature_vector,labels22,testNum=.3):
    X_train, X_test, y_train, y_test = train_test_split(feature_vector, labels22, test_size=testNum, random_state=0)


    clf = LinearDiscriminantAnalysis()
    score4 = cross_val_score(clf, feature_vector, labels22, cv=5)
    accuracy.update({'lda with cross validation ':score4.mean()*100})
    clf.fit(X_train,y_train)
    y_pred=clf.predict(X_test)
    accuracy.update({'lda':metrics.accuracy_score(y_test, y_pred)*100})
    

################################## svm ################################
def liners(feature_vector,labels22,testNum=.3):
    X_train, X_test, y_train, y_test = train_test_split(feature_vector, labels22, test_size=testNum, random_state=0)

    logis = LogisticRegression(max_iter=2500)
    score1 = cross_val_score(logis, feature_vector, labels22, cv=5)
    accuracy.update({'LogisticRegressioncross':score1.mean()*100})
    end=logis.fit(X_train,y_train)
    y_pred=logis.predict(X_test)
    accuracy.update({'LogisticRegression   ':metrics.accuracy_score(y_test, y_pred)*100})
    
#################################  all in  one ###############################################
def classification(feature_vector,labels22,testNum=.3):
    X_train, X_test, y_train, y_test = train_test_split(feature_vector, labels22, test_size=testNum, random_state=0)
    svmcl(feature_vector,labels22,testNum=.3)
    knncl(feature_vector,labels22,testNum=.3)
    mlpcl(feature_vector,labels22,testNum=.3)
    ldacl(feature_vector,labels22,testNum=.3)
    liners(feature_vector,labels22,testNum=.3)
    return accuracy
    