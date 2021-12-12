import numpy as np

x = np.array([[1, 0, 0], [0, 1, 0], [-0.5, 0, 1]])
y = np.linalg.inv(x)  # return the inverse matrix
print(x)
print(y)
print(np.dot(x, y))
