
'''
Pattern 10
          * 
        * * *
      * * * * *
    * * * * * * *
  * * * * * * * * *
    * * * * * * *
      * * * * *
        * * *
          *
'''
num=int(input("Enter range = "))
for i in range(num-1):
    for j in range(num-i):
        print(' ',end=" ")
    for k in range(num-j):
        print('*',end=" ")
    for l in range(i):
        print('*',end=" ")
    print()
for i in range(num):
    for j in range(i+1):
        print(' ',end=" ")
    for j in range(i,num):
        print('*',end=" ")
    for j in range(i,num-1):
        print('*',end=" ")
    print()