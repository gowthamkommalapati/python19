import numpy as np

x = np.array([['Sunny','Warm','Normal','Strong','Warm','Same','Yes'],['Sunny','Warm','High','Strong','Warm','Same','Yes'],
              ['Rainy','Cool','High','Strong','Warm','Change','No'],['Sunny','Warm','High','Strong','Cool','Change','Yes']])

r,c = x.shape
print("The number of rows and columns are: ",r,"and",c-1)

print("The dataset in a training sample is: \n")
print(" Sky Airtemp Humidity Wind Water Forecast EnjoySPORT")
print(x)

s = []
s = np.empty(c-1,dtype=object)
for i in range(c-1):
    s[i] = "\u03A6"
print("\n Initialized more specific hypothesis: \n",s)
for i in range(c-1):
    s[i] = x[0,i]
print("Hypothesis after Processing 1st training sample",s)
for i in range(1,r):
    if x[i,c-1] == "No":
        continue
    else:
        for j in range(c-1):
            if x[i,j]!= s[j]:
                s[j] = '?'

print("\n Intermediate Hypothesis: \n",s)
print("\n Final Maximum Specific Hypothesis: \n",s)

print("Enter new instance value")
new = []
new = np.empty(c-1, dtype=object)
print("Enter Attribute Values for Sky,Airtemp,Humidity,Wind,Water and Forecast")
for i in range(c-1):
    new[i] = input("enter attribute values: ")
print("\nthe given instance is",new)
flag=1
for i in range(c-1):
    if s[i]!='?' and s[i]!= new[i]:
        flag=0
        break
print("\n The assigned label for ENJOYING SPORT is")
if flag==1:
    print("YES")
else:
    print("NO")
        
                
