import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor

np.random.seed(0)
X = np.sort(5 * np.random.rand(40,1), axis=0)
y = np.sin(X).ravel()
y[::5] += 3*(0.5-np.random.rand(8))

model = DecisionTreeRegressor(max_depth=2)

model.fit(X,y)

X_test = np.arange(0.0,5.0,0.01)[:,np.newaxis]
y_pred = model.predict(X_test)
plt.scatter(X,y,color = 'blue',label ='Data')
plt.plot(X_test,y_pred,color = 'red',linewidth =2, label ="Decision Tree Regression")
plt.xlabel('X')
plt.xlabel('y')
plt.title('Decision Tree Regression')
plt.legend()
plt.show()