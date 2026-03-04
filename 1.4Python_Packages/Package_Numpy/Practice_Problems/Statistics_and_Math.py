'''
Given two arrays a and b, add them element-wise.
Multiply every element of an array by 5.
Find the dot product of two 3×3 matrices.
Normalize a random 5×5 matrix.
Find the mean, median, and standard deviation of an array.
Compute the Euclidean distance between two arrays.
Find the most frequent value in a NumPy array.
Compute the covariance matrix of a random dataset.
'''
import numpy as np
# Given two arrays a and b, add them element-wise.
array1=np.array([1,2])
array2=np.array([3,4])
print(np.add(array1,array2))

# Multiply every element of an array by 5.
array3=np.array([[1,2],[3,4]])
scale=5
print(array3*scale)

# Find the dot product of two 3×3 matrices.
array1 = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

array2 = np.array([[9, 8, 7],
                   [6, 5, 4],
                   [3, 2, 1]])
print(np.dot(array1,array2))
print(array1@array2)

# Normalize a random 5×5 matrix.
array=np.random.randint(1,25,size=25).reshape(5,5)
print(array)
min=np.min(array)
max=np.max(array)
normalized_array=(array-min)/(max-min)
print(np.round(normalized_array))

# Find the mean, median, and standard deviation of an array.
print(np.mean(array1),np.median(array1),round(np.std(array1),2))

# Compute the Euclidean distance between two arrays.
distance = np.linalg.norm(array1 - array2) 
print(round(distance,2))

# Find the most frequent value in a NumPy array.
array = np.array([1, 2, 2, 3, 4, 4, 4, 5])
unique, counts = np.unique(array, return_counts=True)
most_frequent = unique[np.argmax(counts)]
print(unique[np.argmax(counts)])

# Compute the covariance matrix of a random dataset.
arr=np.random.rand(5,3)
cov_matrix = np.cov(arr, rowvar=False)
print(cov_matrix)