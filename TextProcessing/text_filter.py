banned = input().split(', ')
text = input()
for ele in banned:
    while ele in text:
        text = text.replace(ele, '*' * len(ele))
print(text)
