'''
Pattern 9
  * * * * * * * * * 
    * * * * * * *
      * * * * *
        * * *
          *
'''
num=int(input("Enter range = "))
for i in range(num):
    for j in range(i+1):
        print(' ',end=" ")
    for j in range(i,num):
        print('*',end=" ")
    for j in range(i,num-1):
        print('*',end=" ")
    print()