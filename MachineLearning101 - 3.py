import numpy as np

#11. Get the common items between a and b

a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
c = np.intersect1d(a,b)
print(c)

#12. How to remove from one array those items that exist in another?
a = np.array([1,2,3,4,5])
b = np.array([5,6,7,8,9])
c = np.setdiff1d(a,b)  #from 'a', remove all of 'b'
print(c)

#13. How to get the positions where elements of two arrays match?

a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
c = np.where(a==b)
print(c)

#14. How to extract all numbers between a given range from a numpy array?

a = np.arange(15)
b = np.where((a>=5) & (a<=10))
print(b)

#15. How to make a python function that handles scalars to work on numpy arrays?

def maxx(x, y):
    """Get the maximum of two items"""
    if x >= y:
        return x
    else:
        return y

pair_max = np.vectorize(maxx, otypes=[float])

a = np.array([5, 7, 9, 8, 6, 4, 5])
b = np.array([6, 3, 4, 8, 9, 7, 1])
print(pair_max(a, b))

#> 5



