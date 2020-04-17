import numpy as np


# reorganizing array
before= np.array([[1,2,3,4],[4,5,6,7]])

after = before.reshape(4,2)


print(after)

#vertically stacking vectors
v1 = np.array([1,2,3,4])
v2 = np.array([5,6,7,8])
v = np.vstack([v1,v2])
vv = np.vstack([v1,v2,v1,v2])
print(v)
print(vv)