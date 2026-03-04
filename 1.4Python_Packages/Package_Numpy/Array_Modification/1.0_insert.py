import numpy as np
# Insert in 1-D Array
array1=np.array([10,30,40,50,60])
new_array1=np.insert(array1,1,20)
print(array1)
print(new_array1)

# Insert in 2-D Array 
two_d_array1=np.array([[10,20,30],[40,50,60]])
new_array1=np.insert(two_d_array1,2,[70,80,90],axis=0)          #row
new_array2=np.insert(new_array1,3,[70,80,100],axis=1)           #column
print(two_d_array1)
print(new_array1)
print(new_array2)

new_array3=np.insert(new_array2,3,[70,80,100],axis=None)     #Flatten
print(new_array3)