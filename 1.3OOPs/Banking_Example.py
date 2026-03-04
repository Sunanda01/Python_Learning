class BankAccount:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance

    def __str__(self):
        return(f"Account Created!!!!!!!\nAccount Holder=> {self.name}\nBalance=> {self.balance}")

    def deposit(self,amount):
        prevBalance=self.balance
        self.balance+=amount
        self.displayMessage(prevBalance)

    def withdraw(self,amount):
        if(amount>self.balance):
            print(f"Insufficient Balance!!!!!!!!")
        else:
            prevBalance=self.balance
            self.balance-=amount
            self.displayMessage(prevBalance)

    def displayMessage(self,prevBalance):
        print(f"Customer Name=> {self.name}\nPrevious Balance=> {prevBalance}\nUpdated Balance=> {self.balance}\nTHANK YOU!!!!!!!!!! VISIT AGAIN!!!!!!!!")

name=input("Enter your name=> ")
balance=int(input("Enter the amount to start your bank account=> "))
b1=BankAccount(name,balance)
print(b1)
flag=True
while flag:
    choice=int(input("\nEnter \n1 To Deposit\n2 To Withdraw\n0 to exit\n"))
    if(choice==1):
        amount=int(input("Enter the amount you want to deposit=>\t"))
        b1.deposit(amount)
    elif(choice==2):
        amount=int(input("Enter the amount you want to withdraw=>\t"))
        b1.withdraw(amount)
    elif(choice==0):
        flag=False
    else:
        print("INVALID iNPUT!!!!!!!!!!! TRY AGAIN!!!!!!!!!!!!")
        flag=False
