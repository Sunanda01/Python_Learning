a=10
b=10
print(a==b)     #True
print(id(a), id(b)) #140730640975048 140730640975048
print(a is b)   #True

c=10
d='10'
print(c!=d)
print(c is not d)

print(c==int(d)) #true

print(id(a) == id(d)) #False