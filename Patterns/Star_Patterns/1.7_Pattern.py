'''
Pattern 8
          * 
        * * *
      * * * * *
    * * * * * * *
  * * * * * * * * *           
'''
num=int(input("Enter range = "))
for i in range(num):
    for j in range(num-i):
        print(' ',end=" ")
    for k in range(num-j):
        print('*',end=" ")
    for l in range(i):
        print('*',end=" ")
    print()