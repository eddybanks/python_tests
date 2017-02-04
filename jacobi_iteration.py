import numpy as np

A = np.array([[4, -1, -1, 0],[-1, 4, 0, -1],[-1, 0, 4, -1],[0, -1, -1, 4]])
b = np.array([[1],[2],[0],[1]])


print(A)
print(b)
print(np.dot(A,b))
