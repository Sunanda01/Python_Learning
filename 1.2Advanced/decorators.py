# Function Copy
def welcome():
    print("Welcome")
wel=welcome()
del welcome
wel

# Closures
def outer(msg):
    def inner():
        print(f"Hello\n{msg}")
    return inner()
outer("How are you?")

# Closure + initial decorators
def outer(func):
    def inner():
        return func([1,2,3,4,5])
    return inner()
print(outer(len))

#Decorators
def demo_func(func):
    def wrapper(*args,**kwargs):
        print("Before Decorator")
        func(*args,**kwargs)
        print("After Decorator")
    return wrapper

@demo_func
def myDecorator(topic):
    print(f"Learning {topic}")
myDecorator('Decorators')