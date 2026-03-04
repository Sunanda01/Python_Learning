'''
Create a 1D array of numbers from 0 to 9.
Create a 3×3 array with all elements equal to 7.
Create an array of 10 random integers between 1 and 100.
Create an array of 20 evenly spaced numbers between 5 and 50.
Create a 4×4 identity matrix
Create a 3×3 matrix with values ranging from 0 to 8.
Create a 5×5 matrix with values 1, 2, 3, 4 just below the diagonal.
'''
import numpy as np
# Create a 1D array of numbers from 0 to 9.
array1=np.arange(0,10,1)
print(array1)

# Create a 3×3 array with all elements equal to 7.
array2=np.full((3,3),7)
print(array2)

# Create an array of 10 random integers between 1 and 100.
array3=np.random.randint(1,101,size=10)
print(array3)

# Create an array of 20 evenly spaced numbers between 5 and 50.
array4=np.arange(5,51,20)
print(array4)
array4 = np.linspace(5, 50, 20)
print(array4)

# Create a 4×4 identity matrix
array5=np.eye(4)
print(array5)

# Create a 3×3 matrix with values ranging from 0 to 8.
array6 = np.arange(9).reshape(3, 3)
print(array6)

# Create a 5×5 matrix with values 1, 2, 3, 4 just below the diagonal.
values=np.arange(1,5)
array8=np.diag(values,-1)
print(array8)