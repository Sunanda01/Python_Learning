# Multiplication
print(5 * 3)     # 15
print("Hi" * 3)  # HiHiHi  (string repetition)

# Unpacking in Function Calls
def add(a, b, c):
    print(a + b + c)
nums = [1, 2, 3]
add(*nums)  # Same as add(1, 2, 3)

# Packing Arguments into a Tuple
def greet(*names):
    print(names)

greet("Alice", "Bob", "Charlie")
# ('Alice', 'Bob', 'Charlie')

# Unpacking in Variable Assignment
a, *b, c = [1, 2, 3, 4, 5]
print(a)  # 1
print(b)  # [2, 3, 4]
print(c)  # 5

# Double Asterisk (**)
def details(**kwargs):
    print(kwargs)
details(name="Alice", age=25)
# {'name': 'Alice', 'age': 25}
data = {"name": "Bob", "age": 30}
details(**data)  
