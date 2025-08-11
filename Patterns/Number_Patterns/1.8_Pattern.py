'''
Pattern 9
5 4 3 2 1 
  4 3 2 1 
    3 2 1
      2 1
        1
'''
num=5
num2=5
for i in range(num):
    p=num2
    for j in range(i):
        print(' ',end=" ")
    for k in range(i,num):
        print(p,end=" ")
        p-=1
    num2-=1
    print()