'''
Pattern 6
Z Z Z Z Z 
  0 0 0 0 
    Z Z Z
      0 0
        Z
'''
num=5
pos=65
for i in range(num):
    for j in range(i):
            print(' ',end=" ")
    for k in range(i,num):
        if i%2==0:
             print(chr(90), end=" ")
        else:
             print(chr(48),end=" ")
    print()