import numpy as np
array1=np.array([1,2,np.nan,4,5,np.nan])
print(np.isnan(array1))      #[False False  True False False  True]

# nan to num
cleaned_arr=np.nan_to_num(array1)
print(cleaned_arr)
cleaned_arr1=np.nan_to_num(array1,nan=5)
print(cleaned_arr1)

# handle infinite value
array2=np.array([1,2,np.inf,4,5,-np.inf])
print(np.isinf(array2))         #[False False  True False False  True]
cleaned_arr2=np.nan_to_num(array2,posinf=100,neginf=-100)
print(cleaned_arr2)
