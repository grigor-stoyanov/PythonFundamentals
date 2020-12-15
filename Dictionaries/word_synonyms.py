n = int(input())
dic = {}
for i in range(0, n):
    word = input()
    synonym = input()
    if word not in dic:
        dic[word] = [synonym]
    else:
        dic[word].append(synonym)
for key, value in dic.items():
    print(f'{key} - {", ".join(value)}')
