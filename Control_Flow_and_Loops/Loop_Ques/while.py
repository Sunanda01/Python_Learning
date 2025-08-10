# Print cube of number fro 1 to 5
num=1
while num<=5:
    print(num**3,end=" ")
    num+=1

# Print product from 1 to 5
num,product=1,1
while num <=5:
    product*=num
    num+=1
print(product)

# Reverse words of a sentence
sentence="Hello World"
word=sentence.split(' ')
print(len(word))
length=len(word)
i=0
while i<length:
    j=len(word[i])-1
    while j>=0:
        print(word[i][j],end="")
        j-=1
    print(end=" ")
    i+=1

# Count constants
vowel='aeiou'
word=input("Enter the word => ")
i,count=0,0
while i<len(word):
    if word[i].lower() not in vowel and word[i].isalpha():
        count+=1
    i+=1
print(count)

# First five multilple of a number
num=int(input("Enter a number to find first five multiple = "))
i=1
while i<=5:
    print(i*num,end=" ")
    i+=1

# Calculate pow of a number
base=int(input("Enter a base number = "))
exponent=int(input("Enter a exponent number = "))
print(base**exponent)
i,power=1,1
while i<=exponent:
    power*=base
    i+=1
print(power)

# Check isSquare
num=int(input("Enter a number to check whether perfect square or not = "))
i=1
isSquare=False
while i*i <=num:
    if i*i==num:
        isSquare=True
    i+=1
if isSquare==True:
    print(f"{num} is a perfect square")
else:
    print(f"{num} is not a perfect square")

# Occurrences of specific character
word=input("Enter the word = ")
letter=input("Enter a character to count = ")
i=0
count=0
while i<len(word):
    if letter.lower()==word[i].lower():
        count+=1
    i+=1
print(count)