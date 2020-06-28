import numpy as np

a = np.array([1,2])
b = np.array([2,1])

dot = 0
for e,f in zip(a,b):
    dot += e*f

print(dot)

print(np.sum(a*b))   #dot productı direkt veriyor.

print(np.dot(a,b)) #dot product veriyor yine.

print(a.dot(b))

#calculating the length::

amag = np.sqrt((a*a).sum())  #a magnitude (uzunluk)
print(amag)

amag = np.linalg.norm(a)  # bu da uzunluk veriyor.

cosangle = a.dot(b) / (np.linalg.norm(a) * np.linalg.norm(b))

angle = np.arccos(cosangle)
print(angle)


