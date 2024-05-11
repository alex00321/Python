import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor

np.random.seed(0)
X = np.sort(5 * np.random.rand(40,1), axis=0)
y = np.sin(X).ravel()
y[::5] += 3*(0.5-np.random.rand(8))

model = RandomForestRegressor(n_estimators=10,random_state=0)

model.fit(X,y)

X_test = np.arange(0.0,5.0,0.01)[:,np.newaxis]
y_pred = model.predict(X_test)
plt.scatter(X,y,color = 'blue',label ='Data')
plt.plot(X_test,y_pred,color = 'red',linewidth =2, label ="Random Forest Regression")
plt.xlabel('X')
plt.xlabel('y')
plt.title('Random Forest Regression')
plt.legend()
plt.show()