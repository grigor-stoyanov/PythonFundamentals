line = input().split()
char_dic = {}
for word in line:
    for char in range(0, len(word)):
        if word[char] not in char_dic:
            char_dic[word[char]] = 1
        else:
            char_dic[word[char]] += 1
for key, value in char_dic.items():
    print(f'{key} -> {value}')
