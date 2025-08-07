def add(a,b):
    return a+b
def callfunc(func):
    return func(10,20)
print(callfunc(add))

def add(a,b):
    def cal():
        return a+b
    return cal
result=add(10,20)
print(result())
