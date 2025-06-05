import numpy as np

a = np.array([1, 2, 3, 4, 5, 6])
print("Przed reshapem -> ",a)
a = a.reshape(1,-1)
print("Po reshapie -> ",a)
a1 = np.array([[1, 1, 1, 9, 9, 9]])

a2 = np.hstack((a, a1))
print(a2)
