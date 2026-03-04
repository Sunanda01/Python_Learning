# Reverse a word
word=input("Enter the word => ")
rev_word=''
length=len(word)
for i in range(length,0,-1):
    print(word[i-1], end="")
    rev_word+=word[i-1]
print(f"Reversed Word is {rev_word}")

# Count number of vowels
vowel='aeiou'
word=input("Enter the word => ")
count=0
for i in word:
    if i in vowel:
        count+=1
print(count)

# Fibonacci of a number
a=0
b=1
print(a,b,end=" ")
for _ in range(8):
    next_num=a+b
    print(next_num,end=" ")
    a,b=b,next_num

# Factorial of a number    
num=int(input("Enter num to find factorial => "))
fact=1
for i in range(1,num+1):
    fact*=i
print(f"{num}! = {fact}")

# Check prime or Not
flag=True
num=int(input("Enter num to check whether prime or not => "))
for i in range(2,int(num**0.5)+1):
    if num%i==0:
        flag=False
if flag and num>1:
     print("Prime")
else:
    print("Not Prime")

# Count the occurrences of char in a word
word_dict={}
word=input("Enter the word => ")
for c in word:
    if c in word_dict:
        word_dict[c]+=1
    else:
        word_dict[c]=1
for i in word_dict:
    print(f"{i} : {word_dict[i]}")