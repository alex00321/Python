import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsRegressor

np.random.seed(0)
X = np.sort(5 * np.random.rand(40,1), axis=0)
y = np.sin(X).ravel()
y[::5] += 3*(0.5-np.random.rand(8))

model = KNeighborsRegressor(n_neighbors=5)

model.fit(X,y)

X_test = np.arange(0.0,5.0,0.01)[:,np.newaxis]
y_pred = model.predict(X_test)
plt.scatter(X,y,color = 'blue',label ='Data')
plt.plot(X_test,y_pred,color = 'red',linewidth =2, label ="K-Nearest Neighbors Regression")
plt.xlabel('X')
plt.xlabel('y')
plt.title('K-Nearest Neighbors Regression')
plt.legend()
plt.show()