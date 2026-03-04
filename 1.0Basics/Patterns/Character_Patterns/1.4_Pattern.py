'''
Pattern 5
A 
B B 
A A A
B B B B
A A A A A
'''
num=5
pos=65
for i in range(1,num+1):
    for j in range(i):
        if i%2==0:
            print(chr(pos+1),end=" ")
        else:
            print(chr(pos),end=" ")
    print()