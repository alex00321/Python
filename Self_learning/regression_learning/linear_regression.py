import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

X = np.array([1,2,3,4,5]).reshape(-1,1)
y = np.array([2,3,4,5,6])

model = LinearRegression()

model.fit(X,y)

print("slope:",model.coef_[0])
print("intecept:",model.intercept_)

plt.scatter(X,y,color = 'blue')
plt.plot(X,model.predict(X),color = 'red',linewidth =2)
plt.xlabel('X')
plt.xlabel('y')
plt.title('Linear Regression')
plt.show()