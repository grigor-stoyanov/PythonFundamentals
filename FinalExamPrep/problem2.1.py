import re


n = int(input())
regex = r'^([$%])(?P<tag>[A-Z][a-z]{2,})\1:\s(\[\d+\]\|){3}$'
for _ in range(n):
    message = input()
    match = re.match(regex, message)
    if match:
        code = re.findall(r'\d+', message)
        code = [chr(int(ele)) for ele in code]
        print(f'{match.group("tag")}: {"".join(code)}')
    else:
        print('Valid message not found!')