import numpy as np
a=np.array([1,2,3,4])
b=np.array([5,2,3,6])
print a[0]
#the code below will print a array of boolena true and false with the help of those we can decide some special elements to choose
print a>2
#Now here the inside [a>2] will give array of booleans with help of it only the elements will be chosen at whose index the value of a>2 is #true
print a[a>2]
print b[a>2]
