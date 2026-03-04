'''
Pattern 4
A 
C C 
E E E
G G G G
I I I I I
'''
num=5
pos=65
for i in range(num):
    for j in range(i+1):
        print(chr(pos),end=" ")
    pos+=2
    print()