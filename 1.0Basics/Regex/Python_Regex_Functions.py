import re

text = "Hello World"
pattern = r"Hello"
match = re.match(pattern, text)
if match:
    print("Matched:", match.group())

text = "Say Hello to the World"
pattern = r"Hello"
match = re.search(pattern, text)
if match:
    print("Found at position:", match.start())

text = "cat bat mat cat bat"
pattern = r"\b\w{3}\b"  
matches = re.findall(pattern, text)
print(matches)

text = "cat bat mat"
pattern = r"\b\w{3}\b"
for m in re.finditer(pattern, text):
    print(m.group(), "found at", m.start())

text = "I like cats and cats are cute"
pattern = r"cats"
new_text = re.sub(pattern, "dogs", text)
print(new_text)

text = "apple,banana;grape|mango"
pattern = r"[;,|]"
parts = re.split(pattern, text)
print(parts)