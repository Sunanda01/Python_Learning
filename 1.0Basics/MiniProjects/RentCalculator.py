print("---------- RENT CALCULATOR ---------- ")
rent=int(input("Enter your house rent=> "))
persons=int(input("Enter the number of persons=> "))
electricity=int(input("Enter electricity bill=> "))
food=int(input("Enter the number of food orders=> "))
sum=0
amount=0
for i in range(0,food):
    amount=int(input(f"Enter price of {i+1} bill=> "))
    sum+=amount
print(f"Total Food Expense=> Rs {sum}/-")
total=rent+food+electricity
share_per_people=total//persons
print(f"Total Expense of {persons} person is Rs {total}/-")
print(f"Share of per people is=> Rs {share_per_people}/-")
print("Thank You!!!!!!!")
