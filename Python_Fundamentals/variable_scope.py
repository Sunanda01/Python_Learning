# a=100
# def display():
#     a=200
#     print(a)
# display()
# print(a)

# a=100
# def update_a():
#     global a
#     a=a+1
#     print(f"Inside func {a}")
# print(f"Before Updating {a}")
# update_a()
# print(f"After Updating {a}")

# for i in range (1,6):
#     print("Inside Loop ",i)
#     a=i**2
#     print(f"square of {i} is {a}")
# print("Outside Loop ",i,a)

# def display():
#     for i in range (1,6):
#         print("Inside Loop ",i)
#         a=i**2
#         print(f"square of {i} is {a}")
# display()
# print("Outside Func ",i,a) #Not accessible

# def sum1(a,b):
#     add=a+b
#     print(add)
# sum1(10,20)
# # print(add) #block scope

#Scope Chain ==LEGB => Local>Enclosing>Global>Built-In
x="global"
def outer():
    x="Outer"
    def inner():
        x="Inner"
        print(x)
    inner()  
outer()

# len="Mango"
def outer():
    def inner():
        print(len("APPLE"))     #TypeError: 'str' object is not callable
    inner()  
outer()
