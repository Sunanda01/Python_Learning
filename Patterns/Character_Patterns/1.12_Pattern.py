'''
Pattern 13
  E D C B A 
    D C B A 
      C B A
        B A
          A
'''
num=5
pos=65

for i in range(num):
    for j in range(i+1):
        print(' ',end=" ")
    for j in range(num-i,0,-1):
        print(chr(pos+j-1),end=" ") 
    print()