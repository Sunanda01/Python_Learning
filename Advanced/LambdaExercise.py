# Square of a Number
square = lambda x: x**2
print(square(6))  # 36

# Add Two Numbers
add = lambda a, b: a+b
print(add(3, 7))  # 10

# Check Even Number
check_even=lambda x:x%2==0
print(check_even(8))
print(check_even(9))

# Reverse a String
reverse = lambda s: s[::-1]     #slice notation meaning “start to end, but step -1” (reverse order).
print(reverse("Python")) 

# Sort List of Tuples by Second Element
pairs = [(1, 2), (4, 1), (9, 0)]
sorted_pairs = sorted(pairs, key=lambda x:x[1])
print(sorted_pairs)  # [(9, 0), (4, 1), (1, 2)]

# Filter Out Odd Numbers
nums = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x:x%2==0, nums))
print(evens)  # [2, 4, 6]

# Multiply Each Number by 3 (Using map)
nums = [1, 2, 3]
triples = list(map(lambda x:x*3, nums))
print(triples)  # [3, 6, 9]

# Get Length of Each Word
words = ["apple", "banana", "kiwi"]
lengths = list(map(lambda w:len(w), words))
print(lengths)  # [5, 6, 4]

# Find Maximum in List of Tuples (by Second Value)
items = [(1, 10), (2, 5), (3, 15)]
max_item = max(items, key=lambda x:x[1])
print(max_item)  # (3, 15)

# Convert List of Strings to Uppercase
words = ["hi", "bye", "yes"]
upper_words = list(map(lambda w:w.upper(), words))
print(upper_words)  # ['HI', 'BYE', 'YES']