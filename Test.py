import numpy as np
import matplotlib.pyplot as plt

# Generating random data
X1 = np.random.randint(1, 100, size=(250,))
Y1 = np.random.randint(1, 100, size=(250,))

# Random sizes and colors for each point
size = np.random.randint(20, 200, size=(250,))  # Size array for each point
colr = np.random.choice(['r', 'b', 'c', 'm', 'g', 'k'], size=(250,))  # Color array for each point

# Creating the scatter plot
plt.scatter(X1, Y1, s=size, c=colr)  # Color and size vary for each point
plt.xlabel("X values")
plt.ylabel("Y values")
plt.show()
