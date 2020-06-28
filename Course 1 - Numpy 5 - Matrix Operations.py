import numpy as np

A = np.array([[1,2],[3,4]])
Ainv= np.linalg.inv(A)

print(Ainv)

print(Ainv.dot(A))

print(np.linalg.det(A))

print(np.diag(A))

print(np.trace(A))

##Eigenvalues

X = np.random.randn(100,3)

cov = np.cov(X.T)
print(cov)

