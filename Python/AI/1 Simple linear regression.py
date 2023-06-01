#Step1   import packages and classes
import numpy as np
from sklearn.linear_model import LinearRegression

#Step2   Provide data
x=np.array([5,15,25,35,45,55]).reshape ((-1,1))
y=np.array([5,20,14,32,22,38])

#Step3   Create a model and fit it
model= LinearRegression()
#\ fit
model.fit(x,y)
model=LinearRegression().fit (x,y)

#Step4   Get results
#\ obtain the coefficient of determination
r_sq=model.score(x,y)
print('Coefficient of determination:', r_sq)
#\ intercept and slope
print("intercept:", model.intercept_)
print("slope:",model.coef_)
# the value b0=5.63 approximately illustrates that youe model predicts the response 6.63 when x is 0
# the value b1=0.54 means the the predicted response rises by 0.54 when x is increased by one

#you can make y 2dimentional array
'''new_model= LinearRegression().fit(x,y.reshape((-1,1)))
print("intercept:", new_model.intercept_)
print("slope:",new_model.coef_)'''

#Step5 Presdict respomse

y_pred=model.predict(x)
print('predicted response:', y_pred, sep='\n')
