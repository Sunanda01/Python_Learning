import re

text='a ab abb abbcc b bba bbaa bbaacc'
print(re.findall(r'ba*',text))
print(re.findall(r'ba+',text))

text="welcome welcc welc"
print(re.findall(r'welcc?',text))

text='o oo ooo oooo ooooo oooooo ooooooo'
print(re.findall(r'o{3}',text))
print(re.findall(r'o{3,}',text))
print(re.findall(r'o{3,6}',text))

text = "<p>Hello</p><p>Python</p>"
# Greedy
print(re.findall(r"<p>.*</p>", text))
# Lazy
print(re.findall(r"<p>.*?</p>", text))

exercise1="cat caat caaat ct"
print(re.findall(r'c.*t',exercise1))
print(re.findall(r'ca+t',exercise1))

exercise2="color colour colouur"
print(re.findall(r'colou?ur',exercise2))
