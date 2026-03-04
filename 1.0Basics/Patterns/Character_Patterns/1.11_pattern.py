'''
Pattern 12
E 
E D 
E D C
E D C B
E D C B A
'''
num=5
pos=65

for i in range(num):
    for j in range(num,num-i-1,-1):
        print(chr(pos+j-1),end=" ") 
    print()