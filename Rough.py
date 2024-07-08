import numpy as np
import matplotlib.pyplot as plt
X1=np.random.randint(1,100,size=(250,))
Y1=np.random.randint(1,100,size=(250,))
size=range(1,60,5)
colr=['r','b','c','m','g','k']
plt.scatter(X1,Y1,s=size,c=colr)
plt.xlabel("X values")
plt.ylabel("Y values")
plt.show()