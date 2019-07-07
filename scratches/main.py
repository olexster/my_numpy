import numpy as np
#import scipy
A = np.array([[1,-2,3],[-1,1,5],[-2,-1,1]])
B = np.array([[ 5, 10,  0]]).T
C = np.linalg.solve(A,B)
print(C)