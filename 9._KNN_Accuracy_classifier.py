import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
data=pd.read_csv('C:\\Users\\ASHISH\\OneDrive\\Desktop\\apndcts.csv')
predictors=data.iloc[:,0:4]
print('Features of training dataset\n',predictors)
print('\n')
target=data.iloc[:,4]
print('Class of IRIS flower \n',target)
print('\n')
predictors_train,predictors_test,target_train,target_test=train_test_split(predictors,target,test_size=0.3,random_state=None)
knn=KNeighborsClassifier(n_neighbors=5)
model=knn.fit(predictors_train,target_train)
accuracy=knn.score(predictors_test,target_test)
print('Accuracy of KNN classifier on IRIS data set',accuracy)
