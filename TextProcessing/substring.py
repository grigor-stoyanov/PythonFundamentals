text1 = input()
text2 = input()
while text1 in text2:
    text2 = text2.replace(text1, '')
print(text2)