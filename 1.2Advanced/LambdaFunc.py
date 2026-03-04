from functools import reduce
add10=lambda x:x+10
print(add10(5))

multiply=lambda a,b:a*b
print(multiply(10,20))

nums=[1,2,3,4,5]
squares=map(lambda x:x**2,nums)
print(list(squares))

nums=[1,2,3,4,5]
filtered=filter(lambda x:x>2,nums)
print(list(filtered))

nums=[1,2,3,4,5]
reduced=reduce(lambda a,b:a*b,nums)
print(reduced)
