import numpy as np
"""An identity array is a square array with ones on its main diagonal. There are two ways to create identity array.

    identy
    eye

"""
a=np.identity(4)
b=np.eye(5, 8, k=1, dtype=int)
print a
print b
