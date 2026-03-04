'''
Pattern 17
C 
C O 
C O D
C O D E
C O D E R
'''
word='CODER'
num=len(word)
for i in range(num):
    for j in range(i+1):
        print(word[j],end=" ")
    print()