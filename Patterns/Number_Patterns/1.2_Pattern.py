'''
Pattern 3
1 
2 2
1 1 1
2 2 2 2
1 1 1 1 1
'''
num=int(input("Enter range = "))
for i in range(num):
    for j in range(i+1):
        if(i%2==0):
            print(1,end=" ")
        else:

            print(2,end=" ")
    print()