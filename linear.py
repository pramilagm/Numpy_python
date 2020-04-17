import numpy as np

# linear algebra
a = np.ones((1,2))
print(a)
b = np.full((3,2),2)
print(b)
# output = np.matmul(a,b)
# print(output)


#To find the determinant

c = np.identity(3)
print(c)
d = np.linalg.det(c)

print(d)
