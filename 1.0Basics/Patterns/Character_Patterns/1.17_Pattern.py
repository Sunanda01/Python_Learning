'''
Pattern 18
R 
R E 
R E D
R E D O
R E D O C
'''
word='CODER'
num=len(word)
for i in range(num):
    for j in range(num,num-i-1,-1):
        print(word[j-1],end=" ")
    print()