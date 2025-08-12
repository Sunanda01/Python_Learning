'''
Pattern 1
A 
A A 
A A A
A A A A
A A A A A
'''
num=5
for i in range(num):
    for j in range(i+1):
        print(chr(65),end=" ")
    print()