'''
Pattern 10
  A B C D E 
    A B C D 
      A B C
        A B
          A
'''
num=5
pos=65
for i in range(num):
    for j in range(i+1):
        print(' ',end=" ")
    for k in range(num-i):
        print(chr(pos+k),end=" ")
    print()