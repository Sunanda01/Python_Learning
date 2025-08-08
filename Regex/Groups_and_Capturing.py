import re
text="John:25, Alice:30"
print(re.findall(r'(\w+):(\d+)',text))

text = "cat bat rat cap"
print(re.findall(r'(?:c|b)at',text))

text = "John:25"
pattern=r'(?P<name>\w+):(?P<age>\d+)'
match=re.search(pattern,text)
print(match.group("name"),match.group("age"))
print(match.groupdict())

text = "Product: Apple, Price: 120"
pattern = r"Product: (\w+), Price: (\d+)"
match=re.search(pattern,text)
print(match.group())
print(match.group(1))
print(match.group(2))
print(match.groups())
print(match.groups())

