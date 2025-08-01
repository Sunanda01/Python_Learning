#Even or Odd calc
num=int(input("Enter a number= "))
if num%2==0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")

#leap year Calculation
year=int(input("Enter any year to chcek whether leap year or not= "))
if(year%4==0):
    if(year%100==0 and year%400==0):
        print(f"{year} is leap year")
    else:
        print(f"{year} is not a leap year")
else:
    print(f"{year} is not a leap year")

#Pizza Order prgm
print("Pizza Order Program")
print("Small Pizza= 100\nMedium Pizza= 200\nLarge Pizza=300\n")
choice=input("Enter s for small, m for medium, l for large =>\t")
sum=0
if(choice=='s' or choice=='S'):
        sum+=100
elif(choice=='m' or choice=='M'):
        sum+=200
elif(choice=='l' or choice=='L'):
   sum+=300 
else:
    print("INVALID CHOICE!!!!!")

add_on=input("Do you want to add Pepperoni\nPlease say Yes or No =>\t")
if(add_on=='Yes' or add_on=='yes'  or add_on=='y'):
        if(choice=='s' or choice=='S'):
            sum+=30   
        elif(choice=='m' or choice=='M' or choice=='l' or choice=='L'): 
              sum+=50
        else:
            print("INVALID CHOICE!!!!!")
extra_chesse=input("Do you want to add Extra Cheese\nPlease say Yes or No =>\t")

if(extra_chesse=='Yes' or extra_chesse=='yes'  or extra_chesse=='y'):
      sum+=20

print(f"Your Total Bill is {sum}")