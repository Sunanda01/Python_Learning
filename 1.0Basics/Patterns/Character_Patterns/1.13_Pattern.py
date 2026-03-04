'''
Pattern 14
          A 
        A B A 
      A B C B A
    A B C D C B A
  A B C D E D C B A
'''
num=5
pos=65

for i in range(num):
    for j in range(num-i):
        print(' ',end=" ")
    for k in range(i+1):
        print(chr(pos+k),end=" ")
    for l in range(i,0,-1):
        print(chr(pos+l-1),end=" ")
    print()