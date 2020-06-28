import numpy as np

#31. How to find the percentile scores of a numpy array?

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris_2d = np.genfromtxt(url, delimiter=',', dtype='object')

i, j = np.where(iris_2d)
np.random.seed(100)
print(iris_2d[np.random.choice((i), 20), np.random.choice((j), 20)])
