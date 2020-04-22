#This Project will be about exploring matrix calculations
import numpy as np

a = np.array([[1,3,5],
             [2,8,9]])
b = np.array([[3,2,8],
             [4,7,1],
             [3,7,8]])
c = a.dot(b)

print(c)
