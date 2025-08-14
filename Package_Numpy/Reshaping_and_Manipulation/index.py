import numpy as np
# Reshaping
print("RESHAPE")
array1=np.array([1,2,3,4,5,6,7,8,9])
print(array1.reshape(3,3))

# Manipulating Array
# Flatten 
print("\nFLATTEN")
array2=np.array([[1,2,3],[4,5,6],[7,8,9]])
flatten_array=array2.flatten()
flatten_array[0]=0
print(flatten_array)
print(array2)
print("\nRAVEL")

# Ravel
array2=np.array([[1,2,3],[4,5,6],[7,8,9]])
ravel_array=array2.ravel()
ravel_array[0]=100
print(ravel_array)
print(array2)