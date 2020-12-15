import re


text = input()
regex = r'(?<!_{2})(?<=_{1})[A-Za-z]+\b'
variables = re.findall(regex, text)
print(','.join(variables))