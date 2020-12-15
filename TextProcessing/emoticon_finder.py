text = input()
emoticons = []
for i in range(0, len(text)):
    if text[i] == ':':
        emoticons.append(':' + text[i+1])
print("\n".join(emoticons))