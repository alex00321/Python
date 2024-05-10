import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import Ridge

X = np.array([[0,0],[0,0.1],[1,1]])
y = np.array([0,0.1,1])

model = Ridge(alpha=1.0)

model.fit(X,y)

print("slope:",model.coef_)
print("intecept:",model.intercept_)

plt.scatter(X[:,0],y,color = 'blue')
plt.plot(X[:,0],model.predict(X),color = 'red',linewidth =2)
plt.xlabel('X')
plt.xlabel('y')
plt.title('Ridge Regression')
plt.show()