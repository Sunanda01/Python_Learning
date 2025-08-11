'''
Pattern 11
          1 
        1 2 1 
      1 2 3 2 1
    1 2 3 4 3 2 1
  1 2 3 4 5 4 3 2 1           
'''
num=5
for i in range(num):
    p=1
    for j in range(num-i):
        print(' ',end=" ")
    for k in range(num-j-1):
        print(p,end=" ")
        p+=1
    for l in range(i+1):
        print(p,end=" ")
        p-=1
    print()