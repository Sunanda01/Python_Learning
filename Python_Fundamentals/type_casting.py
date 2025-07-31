s1=input("Write a string= ")
length=len(s1)
# print(s1 + " has " + length + " characters.")  TypeError: can only concatenate str (not "int") to str
print(s1 + " has " + str(length) + " characters.")
print(type(length))     #<class 'int'>
print(type(str(length)))    #<class 'str'>

# name="a"
# print(10+int(name))           ValueError: invalid literal for int() with base 10: 'a'

name="10"
print(10+int(name))

a=input("Enter 1st num= ")
b=input("Enter 2nd num= ")
print(a+b) #ab
print(int(a)+int(b))

a=int(input("Enter 1st num= "))
b=int(input("Enter 2nd num= "))
print(a+b)