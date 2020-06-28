import numpy as np

a = np.array([[1,2],[3,4],[5,6]])

print(a)
print(a.ndim)  # ndim --> gives number of dimensions
print(a.shape)  #shape veriyor. 2x4'lük gibi. row, column sırasıyla.
print(a.itemsize)
print(a.size)  #number of elements.
print("="*50)
##Accessing/Changing specific elements, rows, columns, etc

a = np.array([[1,2],[3,4],[5,6]])


#getting a specific element [row,column]

print(a[1,1])
print(a[0,0])

print(a[0,:])
print(a[:,1])
a[1,1] = 3
print(a[1,1])
print(a)

##3-D EXAMPLE
print("="*40)
b = np.array([[[1,2],[3,4]], [[5,6], [7,8]]])

print(b)

print(b[0,0,1])