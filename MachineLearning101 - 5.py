import numpy as np
#21. How to print only 3 decimal places in python numpy array?

rand_arr = np.random.random([5,3])

np.set_printoptions(precision=3)
print(rand_arr)

#22. Pretty print rand_arr by suppressing the scientific notation (like 1e10)

np.random.seed(100)
rand_arr = np.random.random([3,3])/1e3
print(rand_arr)

np.set_printoptions(suppress=True)
print(rand_arr)

#23.Limit the number of items printed in python numpy array a to a maximum of 6 elements.
a = np.arange(15)
np.set_printoptions(threshold=6)
print(a)

#24. How to print the full numpy array without truncating
a = np.arange(15)
np.set_printoptions(threshold= np.sys.maxsize)
print(a)

