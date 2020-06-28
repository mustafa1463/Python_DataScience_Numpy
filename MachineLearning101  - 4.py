import numpy as np
#16. How to swap two columns in a 2d numpy array?
arr = np.arange(12).reshape(4,3) #indexlerin sırasını yazıyoruz. columnlar 0,1,2 iken, biz onları 1,0,2 yapalım diyoruz burda. yani 1 ile 0 yer değiştirsin.
print(arr)

arr = arr[:, [1,0,2]]
print(arr)

##17. How to swap two rows in a 2d numpy array?
arr = np.arange(9).reshape(3,3)
print(arr)
arr = arr[[1,0,2],:]  #indexlerin sırasını yazıyoruz. rowlar 0,1,2 iken, biz onları 1,0,2 yapalım diyoruz burda. yani 1 ile 0 yer değiştirsin.
print(arr)

#18. How to reverse the rows of a 2D array?

arr = np.arange(9).reshape(3,3)
print(arr)
arr = arr[::-1]
print(arr)

#19. How to reverse the columns of a 2D array?
print("="*40)
arr = np.arange(9).reshape(3,3)
arr = arr[:,[2,1,0]]
print(arr)

#20. How to create a 2D array containing random floats between 5 and 10?

x = np.random.randint(5,10,size=(5,3))    #bu şekilde integer!
print(x)

y = np.random.uniform(5,10,size=(5,3))
print(y)



