import numpy as np
array1=np.array([10,20,30,40,50,60,70,80])
update_array=np.delete(array1,5)
print(update_array)        

array2=np.array([[0, 1], [1, 2], [2 ,3]])
print("Orginal Array = \n",array2)
update_array=np.delete(array2,[2],0)        #delete row
print("Array after deleting row= \n",update_array)

update_array2=np.delete(update_array,1,axis=1)          #delete column
print("Array after deleting column= \n",update_array2)

