'''
Pattern 15
C 
O O 
D D D
E E E E
R R R R R
'''
word='CODER'
num=len(word)
for i in range(num):
    for j in range(i+1):
        print(word[i],end=" ")
    print()