import re

text = "apple pie, apple tart, banana pie"
pattern = r"apple(?= pie)"
print(re.findall(pattern, text))

text = "apple pie, apple tart, banana pie"
pattern = r"apple(?! pie)"
print(re.findall(pattern, text))

text = "USD100, EUR200, USD300"
pattern = r"(?<=USD)\d+"
print(re.findall(pattern, text))

text = "USD100, EUR200, USD300"
pattern = r"(?<!USD)\d+"
print(re.findall(pattern, text))

