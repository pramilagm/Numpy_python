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

# any other number (full like)
c = np.full_like(a, 2)
print(c)

# random decimal numbers
print(np.random.rand(2, 3))

# random integer number
print(np.random.randint(20, size=(2, 2)))
print(np.random.randint(5, 15, size=(2, 2)))

# the identity matrix
print(np.identity(5))
# repeat the array
arr = np.array([[1, 2, 3]])
print(np.repeat(arr, 3, axis=0))

ar = np.ones((5, 5))

z = np.zeros((3, 3))
z[1, 1] = 9

ar[1:4, 1:4] = z
print(ar)
