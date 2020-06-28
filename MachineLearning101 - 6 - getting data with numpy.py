import numpy as np

iris = np.genfromtxt("iris.data", delimiter=',', dtype='object')
print(iris[:3])
names = ('sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'species')

#Q. Extract the text column species from the 1D iris imported in previous question.
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris_1d = np.genfromtxt(url, delimiter=',', dtype=None)
print(iris_1d.shape)
species = np.array([row[4] for row in iris_1d])
print(species[:5])



#How to convert a 1d array of tuples to a 2d numpy array?

# Input:
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris_1d = np.genfromtxt(url, delimiter=',', dtype=None)

# Solution:
# Method 1: Convert each row to a list and get the first 4 items

iris_2d = np.array([row.tolist()[:4] for row in iris_1d])
iris_2d = iris_2d[:4]
print("="*40)
print(iris_2d)


#28. How to compute the mean, median, standard deviation of a numpy array?

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='object')
sepallength = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0])

print(np.mean(sepallength))
print(np.median(sepallength))
print(np.std(sepallength))

#29. Create a normalized form of iris's sepallength whose values range exactly between 0 and 1 so that the minimum has value 0 and maximum has value 1.

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
sepallength = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0])
Smax, Smin = sepallength.max(), sepallength.min()
S = (sepallength - Smin)/(Smax - Smin)
print(S)

