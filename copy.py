import numpy as np

# coping the arrays and values
a = np.array([1,2,3])
b= a.copy()
b[0] = 20
print(a)

#mathematics operations
z = a+2
print(z)
# subtract each element
print(a-2)

#multiplication 
print(a*2)
#divide each element
print(a/2)

#adding two arrays
c = np.array([2,2,2])
print(a+c)

# square of array element
print(a**2)

#sin and cos 
output = np.cos(a)
print(output)