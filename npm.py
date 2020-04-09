import numpy as np
a = np.array([1, 2, 2])
print(a)

b = np.array([[1.2, 1.3, 1.5], [3.4, 4.6, 5.6]])
print(b)

# get the dimension
print(a.ndim)
print(b.ndim)

# get the shape
print(a.shape)
print(b.shape)

# get the data type
print(a.dtype)
print(b.dtype)
# get the size
print(a.itemsize)

# get total size
print(a.nbytes)
print(b.nbytes)
