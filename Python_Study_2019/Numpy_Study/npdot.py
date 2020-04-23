from numpy import  *
import  numpy as np

d = np.array([[1,2],[3,4]])
print(d)
e = np.array([[5,6],[7,8]])
print(e)
print(np.dot(d,e))
print(np.dot(e,d))
print(np.where(d==1,-1,0))