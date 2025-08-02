tuple1=(10,20,30,40,50,60)
print(tuple1.__contains__(30))

print(tuple1[0::2])
print(tuple1.index(40)+1)
print(tuple1.count(10))
print(len(tuple1))

t=(10,)
print(type(t))
 
tuple2=(10,20,30,(40,50),60)
print(tuple2[len(tuple2)-2])
print(type(tuple2))
# tuple2[len(tuple2)-1]=100         immutable
print(tuple2)

#Tuple To List 
print(list(tuple2))