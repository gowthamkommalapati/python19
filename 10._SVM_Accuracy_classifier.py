import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import svm
data=pd.read_csv('D:\\ENGINEERING\\4.Y\\sem-7\\IT-451 ML Lab\\apndcts.csv')
print('Features supplied for classification')
predictors=data.iloc[:,0:4]
print('\n',predictors)
print('Target class labels')
target=data.iloc[:,4]
print('\n',target)
predictors_train,predictors_test,target_train,target_test=train_test_split(predictors,target,test_size=0.3,random_state=None)
svm=svm.SVC(kernel='linear')
model=svm.fit(predictors_train,target_train)
prediction=svm.predict(predictors_test)
print('Accuracy of SVM classifier', accuracy_score(target_test,prediction,normalize=True))
