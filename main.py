import re

a = 'ldfsdsdl99999999'

b = re.search(r'\d{8}', a)

print(type(b)) # <class 're.Match'>
print(type(b.group(0)))	# <class 'str'>
print(b.group(0)) # 99999999
