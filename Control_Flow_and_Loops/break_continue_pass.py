#Break
num=1
while  num<=10:
    print (num)
    num+=1
    if(num==5):
        print("Loop Break")
        break;
else:
    print("Loop Completed")

print("\n")
#Continue
num=1
while  num<=10:
    print (num)
    num+=1
    if(num==5):
        print("Loop Continue")
        continue;
else:
    print("Loop Completed")
    
#Pass
print("\n")
a=10
while a>=1:
    print(a)
    a-=1
    if(a==5):
        pass
else:
    print("loop completed")
