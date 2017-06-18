import numpy as np
E = np.ones((2,3))
print(E)
F = np.ones((3,4),dtype=int)
print(F)
x = np.array([2,5,18,14,4])
E = np.ones_like(x)
print(E)
Z = np.zeros_like(x)
print(Z)

