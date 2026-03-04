'''
Pattern 1
5 
4 4
3 3 3
2 2 2 2
1 1 1 1 1
'''
num=int(input("Enter range = "))
p=5
for i in range(num):
    for j in range(i+1):
        print(p,end=" ")
    p-=1
    print()