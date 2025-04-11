import re

text:str = "My email is stefano.reali1990@gmail.com"
result:list = re.findall(r'\S+@\S+', text)
print(result)


text = "Rome Paris"
result = re.match(r'[A-Z][a-z]+', text)
print(result.group())


text = "I have 20 cats and 3 dog"
result = re.findall(r'\d+',text)
print(result)