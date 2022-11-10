

#Linear Regression implementation
import pandas as pd  
import numpy as np
import matplotlib.pyplot as plt

def estimate_coef(x, y):
    # number of observations/points
    n = np.size(x)
  
    # mean of x and y 
    mean_x = np.mean(x)
    mean_y = np.mean(y)
    print('\n mean of salary is',mean_x)
    print('\n mean of loan amount is',mean_y)
    print('\n')
    cov=0
    for i in range(n):
        x_d=x[i]-mean_x
        y_d=y[i]-mean_y
        xy=x_d * y_d
        cov=cov+xy
    var=0
    for i in range(n):
        x_d=x[i]-mean_x
        xx= x_d * x_d
        var=var+xx   
            
    
  
    # calculating regression coefficients
    b1 = cov / var
    b0 = mean_y - b1 * mean_x
  
    return (b0,b1)

def plot_regression_line(x, y, b):
    # plotting the actual points as scatter plot
    plt.scatter(x, y, color = "m",
               marker = "o", s = 30)
  
    # predicted response vector
    y_pred = b[0] + b[1] * x
  
    # plotting the regression line
    plt.plot(x, y_pred, color = "g")
  
    # putting labels
    plt.xlabel('Salary in lakhs')
    plt.ylabel('Loan amount in Lakhs')
  
    # function to show plot
    plt.show()


#Import the dataset and define the features

dataframe = pd.read_csv('C:\\Users\\exam3\\Downloads\\reg-dataset.csv', names=['salary','loan_amount_sanctioned'])
print(dataframe)
print('\n')
sal = dataframe.iloc[:,0]
print('The values extraced for SALARY column in lakhs from dataframe')
print(sal)
print('\n')
loanamount = dataframe.iloc[:,1]
print('The values extraced for LOAN AMOUNT in Lakhs column from dataframe')
print(loanamount)
print('\n')

b = estimate_coef(sal, loanamount)
print("Estimated coefficients:\n b0 = {}  \
          \n b1 = {}".format(b[0], b[1]))
print('\n')

print('plot of a straight line')  
# plotting regression line
plot_regression_line(sal, loanamount, b)
print('\n')
print('Enter the salary of a person to predict the loan amount to be sanctioned')
salary1=int(input())
predicted_loan_amount = b[0] + b[1] * salary1
print('loan amount predicted for the entered salary is by Linear Regression: ')
print(predicted_loan_amount) 
