import random
uppercase = [chr(i) for i in range(65, 91)]
lowercase=[chr(i) for i in range(97,123)]
alphabets=uppercase+lowercase
numbers=[chr(i) for i in range(48,58)]
symbols=[chr(i) for i in range(33,48)]

print("Password Generator")
alpha_count=int(input("How many alphabets you want?\t"))
num_count=int(input("How many numbers you want?\t"))
char_count=int(input("How many characters you want?\t"))

password=[]
combined_password=""

for i in range(1,alpha_count+1):
    char=random.choice(alphabets)
    password+=char
for i in range(1,num_count+1):
    char=random.choice(numbers)
    password+=char
for i in range(1,char_count):
    char=random.choice(symbols)
    password+=char
random.shuffle(password)
for i in password:
    combined_password+=i


print(combined_password)