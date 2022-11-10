import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import GaussianNB
data=pd.read_csv("C:\\Users\\exam3\\Downloads\\play_tennis.csv")
print("the given data set is\n")
print(data)
#selection of features
predictors=data.iloc[:,0:4]
#selection class label attribute
target=data.iloc[:,4]
predictors_train,predictors_test,target_train,target_test=train_test_split(predictors,target,test_size=0.3,random_state=123)
gnb=GaussianNB()
model=gnb.fit(predictors_train,target_train)
prediction=model.predict(predictors_test)
print("Accuracy of classifier")
accuracy_score(target_test,prediction,normalize=True)
