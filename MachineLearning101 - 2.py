import numpy as np
#6. How to replace items that satisfy a condition without affecting the original array?

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
out = arr.copy()
out[out%2==1] = -1
print(out)
print(arr)

#7. Convert a 1D array to a 2D array with 2 rows
print("="*40)
x = np.arange(10)
print(x)
x = x.reshape(2,5)
print(x)

#8. How to stack two arrays vertically?
print("="*40)
a = np.arange(10).reshape(2,-1)
b = np.repeat(1, 10).reshape(2,-1)
x = np.vstack([a,b])
print(x)

#9. How to stack two arrays horizontally?
print("="*40)
a = np.arange(10).reshape(2,-1)
b = np.repeat(1, 10).reshape(2,-1)

z = np.hstack([a,b])
print(z)

#10. How to generate custom sequences in numpy without hardcoding?
a = np.array([1,2,3])
a = np.r_[np.repeat(a, 3), np.tile(a, 3)]
print(a)







