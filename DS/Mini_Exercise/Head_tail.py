import random
game=True
while game:
    guess=random.randint(0,1)
    user_guess=int(input("Enter 0 or 1=>\t"))
    if(guess==user_guess):
        if(guess==1):
            print("Heads")
        else:
            print("Tails")
    else:
        print("Wrong Guess")
        game=False
