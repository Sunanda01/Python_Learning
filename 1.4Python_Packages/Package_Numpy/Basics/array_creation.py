import numpy as np
array1=np.array([[1,2,3],[4,5,6]])
print(array1)

# Array with all zeros
array2=np.zeros((2,3))
print(array2)

# Array with all ones
array3=np.ones((3,4))
print(array3)

# Fill array with custom number
array4=np.full((2,2),9)
print(array4)

# Creating sequences of number
array5=np.arange(1,10,2)
print(array5)

# Creating Identiti Matrix
identity_matrix=np.eye(2)
print(identity_matrix)