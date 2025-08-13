import sys
# def mygenerator():
#     yield 1
#     yield 2
#     yield 3
# g=mygenerator()
# print(next(g))
# print(next(g))
# print(next(g))

# Print sum
# print(sum(g))

# Sorting
# print(sorted(g))

# for i in g:
#     print(i**2)

def fibo(limit):
    list1=[]
    a,b=0,1
    while a < limit:
        list1.append(a)
        a,b=b,a+b
    return list1
list1=fibo(300000)
for i in list1:
    print(i,end=" ")
print('Size= ',sys.getsizeof(list1))
print()

# for i in fib:
#     print(i,end=" ")

def fibonacci(limit):
    a,b=0,1
    while a<limit:
        yield a
        a,b=b,a+b
fib=fibonacci(300000)
for i in fib:
    print(i,end=" ")
print('Size= ',sys.getsizeof(fib))