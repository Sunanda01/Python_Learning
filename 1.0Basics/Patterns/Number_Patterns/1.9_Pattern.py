'''
Pattern 10
1 
2 3 
4 5 6
7 8 9 10
'''
num=5
p=1
for i in range(1,num):
    for j in range(1,i+1):
        print(p,end=" ")
        p+=1
    print()