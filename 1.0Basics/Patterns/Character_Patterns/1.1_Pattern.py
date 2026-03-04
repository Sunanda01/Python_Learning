'''
Pattern 2
A 
B B 
C C C
D D D D
E E E E E
'''
num=5
pos=65
for i in range(num):
    for j in range(i+1):
        print(chr(pos),end=" ")
    pos+=1
    print()