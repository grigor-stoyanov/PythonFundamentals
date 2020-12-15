line = input().upper()
rage_dict = {}
unique = set()
rage_text = ''
key = ''
value = ''
index = 0
while index < len(line):
    if not line[index].isdigit():
        key += line[index]
        value = ''
        unique.add(line[index])
        index += 1
    else:
        while line[index].isdigit():
            value += line[index]
            index += 1
            if index >= len(line):
                break
        rage_dict[key] = rage_dict.get(key, '') + value
        key = ''
rage_dict = {key: int(value) for key, value in rage_dict.items()}
print(f'Unique symbols used: {len(unique)}')
for key, value in rage_dict.items():
    print(key * value, end='')
