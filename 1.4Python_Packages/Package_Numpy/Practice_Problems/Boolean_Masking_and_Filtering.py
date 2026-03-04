'''
Replace all odd numbers in an array with -1.
Extract all numbers from an array that are between 5 and 10.
Create a 2D array of shape (3,3) with random integers and count the number of even numbers.	
From a given array, get all elements divisible by 3.
Replace all values in an array greater than 20 with 20. OR Replace all values in an array that are greater than a given value with the value itself.
Count how many elements in an array are greater than the mean.
Filter out NaN values from an array.
Replace all NaN values in an array with 0.
'''
import numpy as np

# Replace all odd numbers in an array with -1.
arr1=np.arange(10)
arr1[arr1%2!=0]=-1
print(arr1)

# Extract all numbers from an array that are between 5 and 10.
arr2=np.random.randint(1,16,size=15)
print(arr2)
print(arr2[(arr2<=10) & (arr2>=5)])

# Create a 2D array of shape (3,3) with random integers and count the number of even numbers.	
arr3=np.random.randint(1,10,size=9).reshape(3,3)
print('Orginal Array= \n',arr3)
filterd_even_array=arr3[arr3%2==0]
print('Filtered Array= \n',filterd_even_array)
count=np.size(filterd_even_array)
print('Count of Even Number= ',count)

# From a given array, get all elements divisible by 3.
arr4=np.random.randint(1,16,size=15)
print(arr4)
print(arr4[arr4%3==0])

# Replace all values in an array greater than 20 with 20
arr5=np.random.randint(15,30,size=10)
print("Original Array\n",arr5)
arr5[arr5>20]=20
print("After Replacing Array\n",arr5)

# Count how many elements in an array are greater than the mean.
arr6=np.random.randint(20,size=10)
print(arr6)
mean=np.mean(arr6)
print("Mean = ",mean)
arr_count=np.size(arr6[arr6>mean])
print("No of elements greater than the mean",arr_count)

# Filter out NaN values from an array
arr7=np.array([0,1,3,np.nan,6,7,9,np.nan,2,np.nan])
print(arr7[~np.isnan(arr7)])

# Replace all NaN values in an array with 0
arr8=np.array([0,1,3,np.nan,6,7,9,np.nan,2,np.nan])
print(np.nan_to_num(arr8,nan=0))