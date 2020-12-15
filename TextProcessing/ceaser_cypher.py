text = input()
encoded = ''
for ch in text:
    encoded += chr(ord(ch)+3)
print(encoded)