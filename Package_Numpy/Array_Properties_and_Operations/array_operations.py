import numpy as np
array1=np.array([10,20,30,40,50])
print(array1+10)
print(array1+10)
print(array1-1)
print(array1*2)
print(array1**2)

# Aggregation Functiobn
print("Sum = ",np.sum(array1))
print("Maximum= " ,np.max(array1))
print("Minimum= " ,np.min(array1))
print("Average= " ,np.average(array1))
print("Mean= " ,np.mean(array1))
print("Standard Deviation= " ,round(np.std(array1),3))
print("Variance= " ,np.var(array1))
