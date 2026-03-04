'''
Pattern 7
          A 
        B B B 
      C C C C C
    D D D D D D D
  E E E E E E E E E
    F F F F F F F
      G G G G G
        H H H
          I
'''
num=5
pos=65
for i in range(num-1):
    for j in range(i,num):
        print(' ',end=" ")
    for k in range(i+1):
        print(chr(pos),end=" ")
    # pos+=1   
    for k in range(i):
        print(chr(pos),end=" ")
    pos+=1  
    print()
for i in range(num):
    for j in range(i+1):
        print(' ',end=" ")
    for j in range(i,num):
        print(chr(pos),end=" ")
    for j in range(i,num-1):
        print(chr(pos),end=" ")
    pos+=1 
    print()