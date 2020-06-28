import numpy as np

x = np.zeros((2,3))
y = np.ones((2,3))
print(x)
print(y)
z = np.ones((5,5,6))
print(z)

print("="*40)

k = np.full((2,2),99)  #99'lardan oluşan 2ye 2 matris.
print(k)
print("="*40)
h = np.random.rand(4,2)  #rastgele 0 ile 1 arasında sayılar veriyor. matris 4x2
y = np.random.randn(4,2) #yine 4 x 2 matris ancak 0 ve 1 arası değil.
print(h)
print(y)

print("="*40)

l = np.random.randint(-4,8,size=(3,3))   #-4 ile 8 arasında sayılardan oluşan 3x3 matris.
print(l)

i = np.identity(6)  #6x6 identity matrix
print(i)

