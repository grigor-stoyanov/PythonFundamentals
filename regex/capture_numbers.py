import re
text = input()
string = text
while text:
    text = input()
    string += text
numbers = re.findall(r'\d+', string)
print(' '.join(numbers))