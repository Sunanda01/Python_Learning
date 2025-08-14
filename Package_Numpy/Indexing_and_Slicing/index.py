import numpy as np
array1=np.array([[10,20,30,40,50,60]])
print(array1[0,2])

array2=np.array([10,20,30,40,50,60])
# Slicing
print(array2[0::2])
print(array2[::-1])   #Reverse
# Fancy Indexing
print(array2[[1,3,5]])

# Boolean Masking
print(array2[array2%3==0])