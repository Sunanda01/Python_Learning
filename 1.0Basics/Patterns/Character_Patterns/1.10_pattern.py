'''
Pattern 11
          A 
        A B C 
      A B C D E
    A B C D E F G
  A B C D E F G H I

'''
num=5
pos=65

for i in range(num):
    p=0
    for j in range(i,num):
        print(' ',end=" ")
    for k in range(i+1):
        print(chr(pos+p),end=" ") 
        p+=1
    for k in range(i):
        print(chr(pos+p),end=" ")
        p+=1
     
    print()