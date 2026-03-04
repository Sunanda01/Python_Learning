'''
Pattern 3
E 
D D 
C C C
B B B B
A A A A
'''
num=5
pos=65
for i in range(num):
    for j in range(i+1):
        print(chr(pos+num-1),end=" ")
    pos-=1
    print()