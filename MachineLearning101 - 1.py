#1. Import numpy as np and see the version
print("="*40)
import numpy as np
print(np.__version__)
print("="*40)

#2. Create a 1D array of numbers from 0 to 9
print("="*40)
x = np.arange(0,9)
print(x)
print("="*40)

#3. How to create a boolean array?
print("="*40)

y = np.full((3,3),True,dtype=bool)
print(y)
print("="*40)

#4. How to extract items that satisfy a given condition from 1D array?
arr = np.array([0,1,2,3,4,5,6,7,8,9])
arr = arr[ arr % 2 == 1]
print(arr)

#5. How to replace items that satisfy a condition with another value in numpy array?
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
arr[arr%2 == 1] = -1
print(arr)
