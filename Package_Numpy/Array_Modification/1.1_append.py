import numpy as np
array1=np.array([10,20,30])
new_arr=np.append(array1,[40,50,60,70,80,90])
print(new_arr)

array2=np.array([[0,1],[1,2]])
new_arr2=np.append(array2,[[2,3]],axis=0)       #row
print(new_arr2)
new_arr3=np.append(new_arr2,[[4,5,6]],axis=None)
print(new_arr3)