# -*- coding: utf-8 -*-
"""Linear-Polynomial-Logistic.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1sb-LS1i74hz-vts41EhIiGxr3ZglTgpQ
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
import seaborn as sns
from sklearn.linear_model import LinearRegression

df=pd.read_csv('salarydataset.csv')
df.head()

#independent Variable
x=df[['YearsExperience']]

#Dependent Variable
y=df[['Salary']]

#Fit Data into Linear Regression
reg=LinearRegression().fit(x,y)

#Model Score
print("Score", reg.score(x,y))

#Model of Parameters
print("Intercept",reg.intercept_)
print("Coefficient",reg.coef_)

#Predicting Values
y_pred=reg.predict(x)
print("Predicted Values",y_pred)

plt.figure(figsize=(8,6))
plt.scatter(x,y,color='red')
plt.plot(x,y_pred,color='black',linewidth=2)
plt.title("Salary vs. Experience")
plt.ylabel("Salary")
plt.xlabel("Years of Experience")
plt.legend()
plt.show()

# Polynomial Regression #
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

x=df[['YearsExperience']]
y=df[['Salary']]
ploy=PolynomialFeatures(degree=3)
x_ploy=ploy.fit_transform(x)

model=LinearRegression()
model.fit(x_ploy,y)
print(model.score(x_ploy,y))

print(model.coef_)
print(model.intercept_)

y_pred=model.predict(x_ploy)

#plotting
plt.figure(figsize=(8,6))
plt.scatter(x,y,color='blue',label='Actual')
plt.plot(x,y_pred,color='red',label='Logistic Regression')

plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import PolynomialFeatures

#IndVariable
x=df[['YearsExperience']]
#DepVariable
y=df[['Salary']]

threshold=50000
y=(df['Salary']>threshold).astype(int)

model=LogisticRegression()
model.fit(x,y)

probabilities=model.predict_proba(x)[:1]
probabilities