'''
Pattern 16
R 
E E 
D D D
O O O O
C C C C C
'''
word='CODER'
num=len(word)
for i in range(num):
    for j in range(i+1):
        print(word[num-i-1],end=" ")
    
    print()