import re
ex="<p>Hello</p> <p>Python</p> <div>Ignore me</div>"
print(re.findall(r'<p>.*?</p>',ex))

num="12 123 1234 12345 1"
print(re.findall(r'\d{2,4}',num))

ex2="cat car c cart coat cut"
print(re.findall(r'\bc[a-zA-Z]+\b',ex2))

fileName="image.jpg photo.png file.txt icon.jpeg"
print(re.findall(r'\b[a-zA-Z]+\.(?:jpg|png)\b',fileName))

text = "John:25, Alice:30, Bob:22"
pattern=r'(?P<name>\w+):(?P<age>\d+)'
matches=re.finditer(pattern,text)
for m in matches:
    print(m.group("name"),m.group("age"))
result=re.findall(r'(\w+):(\d+)',text)
print(result)

emails = "contact@gmail.com, admin@yahoo.com, user@outlook.com"
match=re.findall(r'@(\w+)\.\w+',emails)
print(match)

html = "<h1>Title</h1> <p>Hello</p> <p>World</p>"
match=re.findall(r'<p>(.+?)</p>',html)
print(match)

numbers = "+91-9876543210, +1-5551234567"
pattern=r'(?P<country>\d+)-(?P<number>\d+)'
match=re.finditer(pattern,numbers)
for i in match:
    print(i.groupdict())

numbers = "+91-9876543210, +1-5551234567"
pattern = r'(?P<country>\d+)-(?P<number>\d+)'
matches = re.finditer(pattern, numbers)
result = [m.groupdict() for m in matches]
print(result)