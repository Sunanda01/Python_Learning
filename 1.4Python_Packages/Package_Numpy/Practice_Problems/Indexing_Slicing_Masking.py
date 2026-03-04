'''
Extract all odd numbers from a given NumPy array.
Replace all negative numbers in an array with 0.
Reverse the order of elements in a 1D array.
Get the first column of a 3×3 array.
Extract all numbers greater than 50 from an array.
Create a checkerboard 8×8 matrix with the help of slicing.
Create a 2D array with 1 on the border and 0 inside.
Create an 8×8 matrix and fill it with a checkerboard pattern using tile().
'''
import numpy as np
# Extract all odd numbers from a given NumPy array.
array1=np.arange(1,100)
print(array1)
print(array1[array1%2!=0])

# Replace all negative numbers in an array with 0.
array2=np.array([-2,1,-1,3,4,-5,-3,-5])
array2[array2<0]=0
print(array2)

# Reverse the order of elements in a 1D array.
array3=np.arange(1,10)
print(array3[::-1])
print(np.flip(array3))

# Get the first column of a 3×3 array.
array4=np.arange(1,10).reshape(3,3)
print(array4)
print(array4[:,0])

# Extract all numbers greater than 50 from an array.
array5=np.array([41,43,45,47,49,51,53,55,57,59,61])
print(array5[array5>50])

# Create a checkerboard 8×8 matrix with the help of slicing.
checkboard=np.zeros((8,8),dtype=int)
checkboard[::2,1::2]=1
checkboard[1::2,::2]=1
print(checkboard)

# Create a 2D array with 1 on the border and 0 inside.
array7=np.zeros((5,5),dtype=int)
array7[:,0]=1
array7[:,-1]=1
array7[0,:]=1
array7[-1,:]=1
print(array7)

# Create an 8×8 matrix and fill it with a checkerboard pattern using tile().
base=np.array([[0,1],[1,0]])
array9=np.tile(base,(4,4))
print(array9)