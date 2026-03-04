'''
Pattern 4
          1 
        2 2 2
      3 3 3 3 3
    4 4 4 4 4 4 4
  5 5 5 5 5 5 5 5 5
    4 4 4 4 4 4 4
      3 3 3 3 3
        2 2 2
          1
'''
num=int(input("Enter range = "))
for i in range(num-1):
    for j in range(num-i):
        print(' ',end=" ")
    for k in range(num-j):
        print(i+1,end=" ")
    for l in range(i):
        print(i+1,end=" ")
    print()
p=num
for i in range(num):
    for j in range(i+1):
        print(' ',end=" ")
    for k in range(i,num):
        print(p,end=" ")
    for l in range(i,num-1):
        print(p,end=" ")
    p-=1
    print()