import re
text="cat scatter category tulips"
print(re.findall(r'\bcat\b',text))
print(re.findall(r'\Blip\B',text))

text="Python PYTHON python"
print(re.findall(r'python',text,re.IGNORECASE))

text = """first line
second line
third line """
print(re.findall(r"third", text, re.MULTILINE))

text = """Hello
World
Welcome
World"""
print(re.findall(r"Hello.*World", text))        
print(re.findall(r"Hello.*World", text, re.DOTALL))  
