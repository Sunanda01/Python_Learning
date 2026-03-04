#Use of f-Strings
age=int(input("Enter your current age= "))
years_left=90-age
days_left=years_left*365
months_left=years_left*12
weeks_left=years_left*52
print(f"Your cureent age is {age}\nYou have \n{days_left} days \n{months_left} months \n{weeks_left} weeks \n{years_left} years to be 90 yrs")