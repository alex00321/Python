import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import ElasticNet
from sklearn.preprocessing import PolynomialFeatures

np.random.seed(0)
X = np.sort(5* np.random.rand(40,1),axis=0)
y = np.sin(X).ravel()
y[::5] += 3*(0.5-np.random.rand(8))

model = ElasticNet(alpha=1.0,l1_ratio=0.5)

poly = PolynomialFeatures(degree=12,include_bias=False)
X_poly = poly.fit_transform(X)

model.fit(X_poly,y)

print("coefficient:",model.coef_)

plt.scatter(X,y,color = 'blue',label ='Data')
plt.plot(X,model.predict(X_poly),color = 'red',linewidth =2, label ="Elastic Net Regression")
plt.xlabel('X')
plt.xlabel('y')
plt.title('Elastic Net Regression')
plt.legend()
plt.show()