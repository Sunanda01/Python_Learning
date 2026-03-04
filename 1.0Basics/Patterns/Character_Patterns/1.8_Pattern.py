'''
Pattern 9
A 
A B 
A B C
A B C D
A B C D E
'''
num=5
pos=65
for i in range(num):
    for j in range(i+1):
        print(chr(pos+j),end=" ")
    print()