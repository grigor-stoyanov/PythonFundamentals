import re

regex = r'(w{3}\.[a-zA-Z0-9\-]+(\.[a-z]+)+)'
sentence = input()
while sentence:
    websites = [el.group() for el in re.finditer(regex, sentence)]
    sentence = input()
    print(*websites, sep='\n')
# while sentence:
#     match = re.findall(regex, sentence)
#     if match:
#         websites.append(match)
#     sentence = input()
# for ele in websites:
#     for website in ele:
#         print(website[0])
