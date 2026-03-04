'''
Reshape a 1D array of size 12 into a 3×4 matrix.
Flatten a multi-dimensional array into 1D.
Stack two arrays vertically and horizontally.
Split an array into 3 equal parts.
Change the shape of an array without changing its data.
Create a meshgrid of x and y values from -5 to 5.
'''
import numpy as np

# Reshape a 1D array of size 12 into a 3×4 matrix.
array1=np.arange(1,13).reshape(3,4)
print(array1)

# Flatten a multi-dimensional array into 1D.
array2=np.array([[ 1,2,3 ,4], [ 5, 6, 7 , 8], [ 9, 10, 11, 12]])
print(array2.flatten())

# Stack two arrays vertically and horizontally
array3=np.arange(1,7).reshape(2,3)
array4=np.arange(7,13).reshape(2,3)
print(np.vstack((array3,array4)))
print(np.hstack((array3,array4)))

# Split an array into 3 equal parts
array5=np.arange(1,10).reshape(3,3)
print(np.split(array5,3))

# Change the shape of an array without changing its data.
array6=np.arange(1,10).reshape(3,3)
print(np.reshape(array6,-1))

# Create a meshgrid of x and y values from -5 to 5
x=np.arange(-5,6)
y=np.arange(-5,6)
X,Y=np.meshgrid(x,y)
print(X)
print(Y)