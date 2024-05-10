import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import Lasso
from sklearn.preprocessing import PolynomialFeatures

np.random.seed(0)
X = np.sort(5* np.random.rand(40,1),axis=0)
y = np.sin(X).ravel()
y[::5] += 3*(0.5-np.random.rand(8))

model = Lasso(alpha=1.0)

poly = PolynomialFeatures(degree=12,include_bias=False)
X_poly = poly.fit_transform(X)

model.fit(X_poly,y)

print("coefficient:",model.coef_)

plt.scatter(X,y,color = 'blue',label ='Data')
plt.plot(X,model.predict(X_poly),color = 'red',linewidth =2, label ="Lasso Regression")
plt.xlabel('X')
plt.xlabel('y')
plt.title('Lasso Regression')
plt.legend()
plt.show()