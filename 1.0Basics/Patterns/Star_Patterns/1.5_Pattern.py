'''
Pattern 6
            * 
          * *
        * * *
      * * * *
    * * * * *
  * * * * * *
'''
num=int(input("Enter range = "))
for i in range(num,0,-1):
    for j in range(i,0,-1):
        print(" ",end=" ")
    for k in range(num-i+1):
        print('*',end=" ")
    print()