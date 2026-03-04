'''
Create a random array of integers and sort it.
Generate a random array and shuffle its elements.
Generate coordinate grids using np.meshgrid() for x and y from 0 to 5.
Create a function using NumPy that returns Fibonacci numbers up to n.
Find the unique values and their counts in a NumPy array.
'''
import numpy as np

# Create a random array of integers and sort it.
arr1=np.random.randint(1,11,size=10)
print(np.sort(arr1))

# Generate a random array and shuffle its elements
arr2=np.random.randint(1,11,size=10)
print(arr2)
np.random.shuffle(arr2)
print(arr2)
print(np.random.permutation(arr2))

# Generate coordinate grids using np.meshgrid() for x and y from 0 to 5
A=np.arange(6)
B=np.arange(6)
print(A,'\n',B)
a,b=np.meshgrid(A,B)
print(a,'\n',b)

# Create a function using NumPy that returns Fibonacci numbers up to n.
def fib(n):
    fib_array=np.array([0,1])
    while fib_array[-1] + fib_array[-2] <=n:
        fib_array=np.append(fib_array,fib_array[-1]+fib_array[-2])
    return fib_array
print(fib(30))

# Find the unique values and their counts in a NumPy array.
arr3=np.random.randint(20,size=20)
print(arr3)
ele_array,count_array=np.unique(arr3,return_counts=True)
print(f"Unique Values= {ele_array}\nCounts= {count_array}")