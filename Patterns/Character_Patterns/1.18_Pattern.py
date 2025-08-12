'''
Pattern 19
  R E D O C 
    E D O C 
      D O C
        O C
          C
'''
word='CODER'
num=len(word)
for i in range(num):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(num-i,0,-1):
        print(word[j-1],end=" ")
    print()