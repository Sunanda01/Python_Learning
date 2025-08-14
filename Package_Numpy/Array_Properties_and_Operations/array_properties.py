import numpy as np
array1=np.array([[1,1,1],[2,2,2]])
print(array1.shape)
print(array1.size)
array2=np.array([1,1,1])
array3=np.array([[[1,1,1],[2,2,2],[3,3,3]]])

# ndim
print(array1.ndim,array2.ndim,array3.ndim)

# dtype
array4=np.array([1.1,1.2,5,6,7])
print(array1.dtype,array4.dtype)
print(array1.dtype==float)   #true/false

# astype
print(array4.dtype)
int_array4=array4.astype(int)
print(int_array4)               #[1 1 5 6 7]
print(int_array4.dtype)