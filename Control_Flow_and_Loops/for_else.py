num=input("Enter list of number to get square= ").split()
square=[]
length=len(num)
for i in range(length):
    num[i]=int(num[i])

for i in range(length):
    square.append(num[i]**2)
else:
    print(f"Square Calculated {square}")
