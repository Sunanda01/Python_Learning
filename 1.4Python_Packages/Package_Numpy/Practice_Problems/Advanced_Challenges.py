'''
Tell if a given NumPy array has any NaN values.
Subtract the mean of each row from a matrix.
Create a 5×5 matrix with row values from 0 to 4.
Create a vector of size 10 with values ranging from 0 to 1, both excluded.
Create a 5×5 matrix with 1s on the border and 0s inside.
Generate a 10×10 array of random numbers and find the maximum value in each row.
Create two arrays A and B and find all common elements.
Create a 1D array of 100 random numbers and find the top 5 largest numbers.
Generate a 10×2 array with random numbers and sort it by the second column.
'''
import numpy as np

# Tell if a given NumPy array has any NaN values.
arr1=np.array([0,1,3,np.nan,6,7,9,np.nan,2,np.nan])
print(np.isnan(arr1).any())

# Subtract the mean of each row from a matrix
arr2=np.arange(9).reshape(3,3)
row_mean=arr2.mean(axis=1,keepdims=True)
print(row_mean)
result=arr2-row_mean
print(result)

# Create a 5×5 matrix with row values from 0 to 4.
arr3=np.arange(5)
arr4=np.tile(arr3,5).reshape(5,5)
print(arr4)

# Create a vector of size 10 with values ranging from 0 to 1, both excluded
arr5=np.linspace(0,1,10,endpoint=False)[1:]
print(arr5)

# Create a 5×5 matrix with 1s on the border and 0s inside.
arr6=np.zeros((5,5))
arr6[0,:]=1
arr6[-1,:]=1
arr6[:,0]=1
arr6[:,-1]=1
print(arr6)

# Generate a 10×10 array of random numbers and find the maximum value in each row.
arr7=np.random.randint(0,100,100).reshape(10,10)
print(arr7)
print(np.max(arr7,axis=1))
print(np.max(arr7,axis=0))              #column

# Create two arrays A and B and find all common elements.
A=np.random.randint(1,20,9).reshape(3,3)
B=np.random.randint(1,20,9).reshape(3,3)
print(A)
print(B)
print(np.intersect1d(A,B))

# Create a 1D array of 100 random numbers and find the top 5 largest numbers.
arr8=np.random.randint(101,size=100)
print(np.sort(arr8))
print(np.sort(arr8)[-5:])
print(np.partition(arr8, -5)[-5:][::-1])
print(np.partition(np.unique_values(arr8),-5)[-5:][::-1])

# Generate a 10×2 array with random numbers and sort it by the second column.
arr9=np.random.randint(100,size=20).reshape(10,2)
print(arr9)
print(arr9[:,1])            #get second column
print(arr9[:,1].argsort())      #sorts the second column and returns the index
print(arr9[arr9[:,1].argsort()])        #access the element from the index