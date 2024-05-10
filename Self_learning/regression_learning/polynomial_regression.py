import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

np.random.seed(0)
X = 2 * np.random.rand(100,1) - 1 
y = 0.5 * X**2 + X+ 2+ np.random.randn(100,1)*0.1

poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)

model = LinearRegression()

model.fit(X_poly,y)

print("intercept:",model.intercept_)
print("coefficient:",model.coef_)

plt.scatter(X,y,color = 'blue',label ='Data')
plt.plot(X,model.predict(X_poly),color = 'red',linewidth =2, label ="Polinomial Regression")
plt.xlabel('X')
plt.xlabel('y')
plt.title('Polinomial Regression')
plt.legend()
plt.show()