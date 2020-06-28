import numpy as np
A = np.array([[1,2],[3,4]])
B = np.array([1,2])

x = np.linalg.inv(A).dot(B)
print(x)
##oorrr

xx = np.linalg.solve(A,B)
print(xx)

