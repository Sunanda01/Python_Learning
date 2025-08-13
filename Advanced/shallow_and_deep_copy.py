import copy
# Shallow Copy
list1=[[1,2],[3,4]]
shallow=copy.copy(list1)
print(f"Before Shallow Copy\n{list1}\n{shallow}")
shallow[0][0]=0
print(f"After Shallow Copy\n{list1}\n{shallow}")

# Deep Copy
list1=[[1,2],[3,4]]
shallow=copy.deepcopy(list1)
print(f"Before Deep Copy\n{list1}\n{shallow}")
shallow[0][0]=0
print(f"After Deep Copy\n{list1}\n{shallow}")

l1=[1,2,3,4]
shallow=copy.copy(l1)
shallow[0]=0
print(l1,shallow)       #[1, 2, 3, 4] [0, 2, 3, 4]
l1=[1,2,3,4]
deep=copy.deepcopy(l1)
deep[0]=0
print(l1,deep)      #[1, 2, 3, 4] [0, 2, 3, 4]