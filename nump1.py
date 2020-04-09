import numpy as np
a = np.array([[1, 2, 3, 4, 5, 6, 7],
              [9, 8, 7, 6, 5, 4, 3]
              ])
print(a)

# get the specific element [r,c]
print(a[1, 2])

# get the specific row
print(a[0, :])

# get the specific column
print(a[:, 3])

# getting a little more fancy[startindex, endindex, stepsize]
print(a[0, 1:6:2])

# Updating element in array
# updating row
a[1, 5] = 20
print(a)
# updating column
a[:, 2] = [15, 16]
print(a)
