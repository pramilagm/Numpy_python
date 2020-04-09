import numpy as np
a = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(a)

# to get the specific element in 3d array
print(a[0, 1, 0])
print(a[1, 0, 0])

a[:, 1, :] = [[9, 9], [8, 8]]
print(a)

# Initializing different types of array
# All zeros matrix
b = np.zeros((2, 3))
print(b)
# all one's matrix
print(np.ones((4, 2, 2), dtype='int32'))
# Any other type
c = np.full((2, 2), 99)
print(c)
