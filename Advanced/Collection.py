from collections import Counter, defaultdict, deque, namedtuple,OrderedDict

# Counter
print(Counter("banana"))

# defaultdict
dd = defaultdict(float)
dd["apple"] += 1
dd['mango']
print(dd)

# deque
dq = deque([1, 2, 3])
dq.appendleft(0)
print(dq)

# namedtuple
Point = namedtuple("Point", ["x", "y"])
p = Point(2, 3)
print(p.x, p.y)

#OrderedDict
dict1=OrderedDict()
dict1['a']=1
dict1['b']=2
dict1['c']=3
dict1['d']=4
dict1['e']=5
print(dict1)