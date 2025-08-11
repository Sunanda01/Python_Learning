'''
Pattern 6
  1 2 3 4 5 
    1 2 3 4 
      1 2 3
        1 2
          1
'''
num=5
for i in range(1,num+1):
    for j in range(1,i+1):
        print(' ',end=" ")
    for k in range(0,num+1-i):
        print(k+1,end=" ")
    print()

