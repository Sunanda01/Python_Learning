import re
text = "cat bat rat apple"
print(re.findall(r"c.t", text))  

text="Hello Morning"
print(re.findall(r"^Hello",text))
print(re.findall(r"Morning$",text))

digit='Su999127nan054d7a'
print(re.findall('\d',digit))
print(re.findall("\D",digit))

word_char="A_*P_+PLE"
print(re.findall(r'\w',word_char))
print(re.findall(r'\W',word_char))

space="S a d h u k   h a n "
print(re.findall(r"\s",space))
print(re.findall(r'\S',space))

text = "den pen hen ten gen len men "
print(re.findall(r"[ghta]en", text))  

text="Sunanda sadhu apple mango"
print(re.findall(r"Sunanda|apple",text))

exercise1="Hello Python"
print(re.findall(r'[aeiouAEIOU]',exercise1))

exercise2="The cat ran far and hit the big log"
print(re.findall(r'\b\w{3}\b',exercise2))