import re

text = input()
emails = r'(?P<user>((?<=[\w\s])\b[a-zA-Z0-9]+[\._\-]+[a-zA-Z0-9]+)@(?P<host>(\w+[\.\-]+)+\w+\b))'
matches = re.finditer(emails, text)
for email in matches:
    print(email.group())

# (^|<=\s) & ($|=\s) also works
# (^|<=\s)([a-zA-Z0-9]+)[\._-]?@(\g<1>[-]?)+(\.\w+)+($|=\s)
# g<2> вика регекса