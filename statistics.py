import numpy as np

#statistics
#to find min and max

a = np.array([[1,2,3],[4,5,6]])
output = np.min(a, axis=1)
outMax = np.max(a)
print(output)
print(outMax)

#to find sum
s = np.sum(a, axis=0)
print(s)
