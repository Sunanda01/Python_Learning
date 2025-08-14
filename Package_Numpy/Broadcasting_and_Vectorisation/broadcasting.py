import numpy as np

# Broadcasting single Vlaue
array1=np.array([100,200,300,400])
discount=10     # scalar
new_array=array1-(array1*discount/100)
print(new_array)

# 1-D to 2-D
matrix=np.array([[10,20],[30,40]])
vector=np.array([10,10])
print(matrix+vector)

matrix=np.array([[10,20],[30,40]])
vector=np.array([10,10,10])
# print(matrix+vector)      error
