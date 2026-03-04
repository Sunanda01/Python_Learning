list1=[1,2,3,[4,5,6,7],8,9,10]
length=len(list1)
print(length)
print(list1[3][-1])
print(list1[length-4][1::2])

list2=[10,20,30,['Apple','Ball','Cat','Dog'],40,50]
print(list2[len(list2)-3][-1])      #Dog